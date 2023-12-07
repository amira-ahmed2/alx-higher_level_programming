#!/usr/bin/python3
"""write file"""


def append_write(filename="", text=""):
    """fun is write file
    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".
    """
    with open(filename, 'a', encoding="utf-8") as f:
        c = f.write(text)
    return c
