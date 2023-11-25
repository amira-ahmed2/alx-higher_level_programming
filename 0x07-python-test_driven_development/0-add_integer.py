#!/usr/bin/python3
"""Defines an integer addition function"""


def add_integer(a, b=98):
    """that fun is sum two integer

    Args:
        a (int or float): one number
        b (int, float): two number. Defaults to 98.

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        int: sun two numbers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)