#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new = []
    for ar in matrix:
        tmp = [x * x for x in ar]
        new.append(tmp)

    return new
