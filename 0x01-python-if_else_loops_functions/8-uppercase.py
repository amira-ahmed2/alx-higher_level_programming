#!/usr/bin/python3
def uppercase(str):
    for i in range(41, 91):
        if ord(str) == i:
            return True
        else:
            continue
    return False
