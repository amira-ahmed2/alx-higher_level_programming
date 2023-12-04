#!/usr/bin/python3
"""function that returns the list
available attributes and
methods of an object
"""
def lookup(obj):
    """function that returns the list
available attributes and
methods of an object

    Args:
        obj (dir): dir

    Returns:
        obj: dir
    """
    return dir(obj)
