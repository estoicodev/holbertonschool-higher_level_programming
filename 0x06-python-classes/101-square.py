#!/usr/bin/python3
"""This module creates a class named Square"""


class Square:
    """A class named Square

    Attributes:
    attr1 (size): size of square
    attr2 (position): position of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
        size (int): size attribute for the instance
        position (tuple): position attribute for the instance
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    def my_print(self):
        """Print the instance of the class Square"""
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for y in range(self.__position[1]):
                    print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    if j == self.__size - 1:
                        print("#")
                    else:
                        print("#", end="")

    @property
    def position(self):
        """Gets the position attribute of the instance of class Square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position attribute of the instance of class Square"""
        if type(value) != tuple or len(tuple) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __repr__(self):
        """Print the instance of the class Square"""
        square_str = ""
        if self.__size > 0:
            for y in range(self.__position[1]):
                square_str += "\n"
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    square_str += " "
                for j in range(self.__size):
                    square_str += "#"
                square_str += "\n"
        else:
            square_str += "\n"
        return square_str
