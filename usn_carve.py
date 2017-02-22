#!/usr/bin/python

import os
import sys
import mmap
import struct

filename = sys.argv[1]

with open(filename, "rb") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    offset = 0
    while True:
        try:
            offset = m.index("\x00\x00\x02\x00\x00\x00", offset)
        except ValueError:
            m.close()
            break

        if m.find("\x00\x3c\x00", offset + 55, offset + 58) == -1:
            offset +=1
            continue

        recordLength = struct.unpack("<i", m[offset - 2:offset + 2])[0]
        if recordLength < 62 or recordLength > 570:
            offset += 1
            continue

        sys.stdout.write(m[offset - 2:(offset - 2) + recordLength])
        offset += (recordLength - 2)
