#!/usr/bin/python3
"""This module defines a Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square
    Attributes:
    id (int): Id of the instance
    width (int): Width of the instance
    height (int): Height of the instance
    x (int): x of the instance
    y (int): y of the instance
        """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes an instance of Square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of the Square class object"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)
