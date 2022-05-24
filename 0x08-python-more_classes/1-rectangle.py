#!/usr/bin/python3
"""This module creates a class named Rectangle"""


class Rectangle:
    """A class named Square

    Attributes:
    attr1 (size): size of square
    attr2 (position): position of the square
    """
    def __init__(self, width=0, height=0):
        """
        Args:
        width (int): width attribute for the instance
        height (int): height attribute for the instance
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """Gets the width of the instance of class Square"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the instance of class Square"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the instance of class Square"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the instance of class Square"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
