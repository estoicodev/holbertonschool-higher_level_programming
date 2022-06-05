"""This module defines a Base class"""


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
