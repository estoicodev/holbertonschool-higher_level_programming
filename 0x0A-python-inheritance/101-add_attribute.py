#!/usr/bin/python3
"""This module defines add_attribute function"""


def add_attribute(obj, name_attr, value_attr):
    """Adds a new attribute to an object if it’s possible
    Args:
    obj (obj): Object
    name_attr (str): Name attribute
    value_attr (str): Value attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name_attr, value_attr)
