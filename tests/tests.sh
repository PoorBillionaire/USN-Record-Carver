#!/usr/bin/env bash

unzip tests/usnjrnl.zip
usncarve.py -h
usn.py -h
usncarve.py -f usnjrnl.bin -o /tmp/usn-carved.bin
echo "[ + ] Carve completed"
echo "[ + ] Attempting to parse carved records"
usn.py -f /tmp/usn-carved.bin -o /tmp/usn-parsed.txt
cat /tmp/usn-parsed.txt
rm /tmp/usn-parsed.txt
usn.py --csv -f /tmp/usn-carved.bin -o /tmp/usn-parsed.txt
cat /tmp/usn-parsed.txt
rm /tmp/usn-parsed.txt
usn.py --verbose -f /tmp/usn-carved.bin -o /tmp/usn-parsed.txt
cat /tmp/usn-parsed.txt
rm /tmp/usn-parsed.txt
usn.py --tln -f /tmp/usn-carved.bin -o /tmp/usn-parsed.txt
cat /tmp/usn-parsed.txt
rm /tmp/usn-parsed.txt
usn.py --tln --system ThisIsASystemName -f /tmp/usn-carved.bin -o /tmp/usn-parsed.txt
cat /tmp/usn-parsed.txt
rm /tmp/usn-parsed.txt
usn.py --body -f /tmp/usn-carved.bin -o /tmp/usn-parsed.txt
cat /tmp/usn-parsed.txt
mactime -b /tmp/usn-parsed.txt
