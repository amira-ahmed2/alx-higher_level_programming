#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    list_set = set()
    for i in set_1:
        if i in set_2:
            continue
        list_set.add(i)
    for j in set_2:
        if j in set_1:
            continue
        list_set.add(j)
    return list_set
