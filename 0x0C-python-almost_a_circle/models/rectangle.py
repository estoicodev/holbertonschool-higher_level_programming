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

    def area(self):
        """Returns the area of the instance Rectangle class"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        for row in range(self.__y):
            print()
        for row in range(self.__height):
            for column in range(self.__x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args):
        """Assigns an argument to each attribute"""
        attributes = ["id", "width", "height", "x", "y"]
        count = len(args)
        for i in range(count):
            setattr(self, attributes[i], args[i])

    def __str__(self):
        """Returns the string representation of the object"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    @property
    def width(self):
        """Returns width of instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set a new width of an instance"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns height of instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set a new height of an instance"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns x of instance"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set a new x of an instance"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns y of instance"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set a new y of an instance"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
