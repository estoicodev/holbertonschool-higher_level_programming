#!/usr/bin/python3
"""This module defines a BaseGeometry class"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """Raises an Exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a positive integer
        Args:
        name (str): Name of the variable
        value (int): Value of the variable
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
