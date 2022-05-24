#!/usr/bin/python3
#!/usr/bin/python3
"""This module creates a class named Rectangle"""


class Rectangle:
    """A class named Square
    Attributes:
    attr1 (width): width of square
    attr2 (height): height of square
    """

    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

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

        Rectangle.number_of_instances += 1

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

    def area(self):
        """Calculates area of the rectangle based on the width and height
        Returns:
        int: Returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates perimeter of the rectangle based on the width and height
        Returns:
        int: Returns the perimeter of the rectangle
        """
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """Print the instance of the class Rectangle"""
        rectangle_str = ""
        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    if j == self.__width - 1 and i != self.__height - 1:
                        rectangle_str += str(self.print_symbol) + "\n"
                    else:
                        rectangle_str += str(self.print_symbol)
        return rectangle_str

    def __repr__(self):
        """Print the string representation of the instance"""
        return f"Rectangle({self.__width}, {str(self.__height)})"

    def __del__(self):
        """Delete the instance of class Rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
