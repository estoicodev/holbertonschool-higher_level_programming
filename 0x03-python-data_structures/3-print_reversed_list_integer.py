#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        rev_list = reversed(my_list)
        for elem in rev_list:
            print(elem)
