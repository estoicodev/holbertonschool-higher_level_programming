#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.

The example module supplies one function, matrix_divided().
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    """

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    size_row = len(matrix[0])
    for i in range(len(matrix)):
        if size_row != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        size_row = len(matrix[i])

        new_row = []
        for j in range(len(matrix[i])):
            elem = matrix[i][j]
            if type(elem) is not int and type(elem) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
            new_row.append(round(elem / div, 2))

        new_matrix.append(new_row)

    return new_matrix
