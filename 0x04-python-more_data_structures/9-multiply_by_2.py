#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dirc = {}
    for k, x in a_dictionary.items():
        new_dirc[k] = x * 2
    return new_dirc
