#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """fun is read file

    Args:
        filename (str, optional): _description_. Defaults to "".
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
