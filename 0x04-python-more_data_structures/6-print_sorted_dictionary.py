#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_key = sorted(a_dictionary.keys())
    for x in sort_key:
        print("{}: {}".format(x, a_dictionary[x]))