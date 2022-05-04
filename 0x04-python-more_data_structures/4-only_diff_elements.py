#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    new_set = set()
    for elem_1 in set_1:
        both = 0
        for elem_2 in set_2:
            if elem_2 == elem_1:
                both = 1
        if both != 1:
            new_set.add(elem_1)

    for elem_2 in set_2:
        both = 0
        for elem_1 in set_1:
            if elem_1 == elem_2:
                both = 1
        if both != 1:
            new_set.add(elem_2)

    return new_set
