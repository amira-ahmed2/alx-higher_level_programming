#!/usr/bin/python3
"""Defines an that prints My name is <first name> <last name>"""


def print_square(size):
    if type(size) is not int:
        raise TabError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
