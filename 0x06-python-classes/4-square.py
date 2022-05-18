#!/usr/bin/python3
"""This module creates a class named Square"""


class Square:
    """A class named Square

    Attributes:
    attr1 (size): size of square
    """
    def __init__(self, size=0):
        """
        Args:
        size (int): size attribute for the instance
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates of the square based on the size
        Returns:
        int: Returns the area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Gets the size of the instance of class Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the instance of class Square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
