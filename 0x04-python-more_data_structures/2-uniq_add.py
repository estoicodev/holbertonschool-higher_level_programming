#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq = []
    sum = 0
    for elem in my_list:
        if elem not in uniq:
            uniq.append(elem)
    for elem in uniq:
        sum += elem

    return sum
