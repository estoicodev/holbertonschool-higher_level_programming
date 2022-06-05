#!/usr/bin/python3
"""This module defines a Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle
    Attributes:
    id (int): Id of the instance
    width (int): Width of the instance
    height (int): Height of the instance
    x (int): x of the instance
    y (int): y of the instance
        """
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance of Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns width of instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set a new width of an instance"""
        self.__width = value

    @property
    def height(self):
        """Returns height of instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set a new height of an instance"""
        self.__height = value

    @property
    def x(self):
        """Returns x of instance"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set a new x of an instance"""
        self.__x = value

    @property
    def y(self):
        """Returns y of instance"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set a new y of an instance"""
        self.__y = value
