#!/usr/bin/python3
def weight_average(my_list=[]):
    # (<score>, <weight>)
    if not my_list:
        return None
    else:
        mul_weight = 0
        sum_weight = 0
        for i in my_list:
            mul_weight += i[0] * i[1]
            sum_weight += i[1]
        return mul_weight / sum_weight