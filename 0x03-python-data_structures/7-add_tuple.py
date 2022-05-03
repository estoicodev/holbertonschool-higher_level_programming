#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 1:
        first_a = tuple_a[0]
        second_a = 0
    elif len(tuple_a) == 0:
        first_a = 0
        second_a = 0
    else:
        first_a = tuple_a[0]
        second_a = tuple_a[1]

    if len(tuple_b) == 1:
        first_b = tuple_b[0]
        second_b = 0
    elif len(tuple_b) == 0:
        first_b = 0
        second_b = 0
    else:
        first_b = tuple_b[0]
        second_b = tuple_b[1]

    new_tuple = (first_a + first_b, second_a + second_b)

    return new_tuple
