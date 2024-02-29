#!/usr/bin/python3
""" finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """that finds a peak in a list of unsorted integers.
    """
    lth = len(list_of_integers)
    s = 0
    e = lth - 1
    if lth == 0:
        return None
    elif lth == 1:
        return list_of_integers[0]

    while s <= e:
        mid = int(e + s)
        last_value = list_of_integers[mid]
        l_value = list_of_integers[mid - 1] if mid - 1 >= 0 else float("-inf")
        r_value = list_of_integers[mid + 1] if mid + 1 < lth else float("-inf")
        if l_value > last_value:
            return l_value
        elif r_value > last_value:
            return r_value
        else:
            return last_value
