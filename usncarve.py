#!/usr/bin/python

from __future__ import print_function

import os
import sys
import mmap
import struct
import contextlib
from argparse import ArgumentParser


def validate_address_space(infile):
    if os.path.getsize(infile) > sys.maxsize:
        print("\n[ - ] ERROR: The running Python process does not present a " \
            "large enough address space to accomodate memory mapping the " \
            "intput file. Try switching to 64-bit Python.\n",
            file=sys.stderr)

def carve_usn_records(infile, outfile):
    with contextlib.closing(mmap.mmap(infile.fileno(), 0, access=mmap.ACCESS_READ)) as m:
        offset = 0
        while True:
            offset = m.find(b'\x00\x00\x02\x00\x00\x00', offset)
            if offset == -1:
                break

            if m.find(b'\x00\x3c\x00', offset + 55, offset + 58) == -1:
                offset +=1
                continue

            offset -= 2
            record_length = struct.unpack('<I', m[offset:offset + 4])[0]
            if record_length < 62 or record_length > 570:
                offset += 3
                continue

            outfile.write(m[offset:offset + record_length])
            offset += (record_length)

def main():
    p = ArgumentParser()
    p.add_argument("-f", "--file", help="Carve USN records from the given file", required=True)
    p.add_argument("-o", "--outfile", help="Output to the given file", required=True)
    args = p.parse_args()

    with open(args.file, "rb") as i:
        with open(args.outfile, "ab") as o:
            try:
                carve_usn_records(i, o)
            except ValueError:
                validate_address_space(args.file)


if __name__ == "__main__":
    main()