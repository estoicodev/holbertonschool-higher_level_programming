#!/usr/bin/python3
"""This module defines a Rectangle class inherited to BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherited to BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation of a Rectangle class
        Args:
        width (int): width instance attribute for the instance
        height (int): height instance  attribute for the instance
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
