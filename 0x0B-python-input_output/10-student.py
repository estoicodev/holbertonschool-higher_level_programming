#!/usr/bin/python3
"""This module defines a class named Student"""


class Student:
    """A class named Student
    Attributes:
    attr1(first_name): first name
    attr2(last_name): last name
    attr3(age): age
    """
    def __init__(self, first_name, last_name, age):
        """Initialization of a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if type(attrs) is list:
            my_dict = {}
            for e in attrs:
                if type(e) is not str:
                    return self.__dict__
                if e in self.__dict__:
                    my_dict[e] = self.__dict__[e]
            return my_dict
        else:
            return self.__dict__
