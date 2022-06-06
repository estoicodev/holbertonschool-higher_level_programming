#!/usr/bin/python3
"""This module defines a Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """class Rectangle inherited by Base class
    Attributes:
    id (int): Id of the instance
    width (int): Width of the instance
    height (int): Height of the instance
    x (int): x of the instance
    y (int): y of the instance
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance of Rectangle class
        Args:
            width (int): Width of the instance Rectangle class
            height (int): Height of the instance Rectangle class
            x (int): x of the instance Rectangle class
            y (int): y of the instance Rectangle class
            id (int): Id of the instance Rectangle class
        Raises:
            TypeError: if width or height is not an integer
            ValueError: if width or height <= 0
            TypeError: if x or y is not an integer
            ValueError: if x or y < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

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

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        attributes = ["id", "width", "height", "x", "y"]
        count = len(args)
        if not args or count == 0:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)
        else:
            for i in range(count):
                setattr(self, attributes[i], args[i])

    def __str__(self):
        """Returns the string representation of the object"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def to_dictionary(self):
        olddict = self.__dict__
        newdict = {}
        for e in olddict:
            key = e.replace("_Rectangle__", "")
            newdict[key] = olddict[e]
        return newdict
