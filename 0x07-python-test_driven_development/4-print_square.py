#!/usr/bin/python3
"""
This is the "4-print_square" module.

The example module supplies one function, print_square().
"""


def print_square(size):
    """
    Prints a square with the character #
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            if j == size - 1:
                print("#")
            else:
                print("#", end="")
