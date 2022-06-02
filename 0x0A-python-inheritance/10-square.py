#!/usr/bin/python3
"""This module defines a Square class inherited to Rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherited to Rectangle class"""
    def __init__(self, size):
        """Instantiation of a Rectangle class
        Args:
        size (int): size instance attribute for the instance
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of instance class Square based on size"""
        return self.__size * self.__size

    def __str__(self):
        """Returns string representation of the instance class Rectangle"""
        return f"[Rectangle] {self.__size}/{self.__size}"
