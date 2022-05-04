#!/usr/bin/python3

def common_elements(set_1, set_2):
    new_set = set()
    for elem_1 in set_1:
        for elem_2 in set_2:
            if elem_1 == elem_2:
                new_set.add(elem_1)

    return new_set
