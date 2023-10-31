#!/usr/bin/python3
for lett in range(122, 96, -1):
    if lett % 2 == 0:
        print("{}".format(chr(lett)), end="")
    else:
        lett -= 32
        print("{}".format(chr(lett)), end="")
