#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max = -99999999
    for i in range(len(my_list)):
        if my_list[i] > max:
            max = my_list[i]

    return max
