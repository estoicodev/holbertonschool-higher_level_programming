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

    @property
    def size(self):
        """Returns size of instance"""
        return self.width

    @size.setter
    def size(self, value):
        """Set a new size for the instance"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute to the Square class"""
        attributes = ["id", "size", "x", "y"]
        count = len(args)
        if not args or count == 0:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)
        else:
            for i in range(count):
                setattr(self, attributes[i], args[i])
