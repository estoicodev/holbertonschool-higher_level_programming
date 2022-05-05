#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(list(a_dictionary))
    for i in range(len(a_dictionary)):
        print(f"{sorted_keys[i]}: {a_dictionary[sorted_keys[i]]}")
