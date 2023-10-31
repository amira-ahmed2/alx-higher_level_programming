#!/usr/bin/python3
for lett in range(97, 123):
    if lett == 101 or lett == 113:
        continue
    print("{}".format(chr(lett)), end="")
