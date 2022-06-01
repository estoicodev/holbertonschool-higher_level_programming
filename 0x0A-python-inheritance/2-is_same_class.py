#!/usr/bin/python3
"""This module defines is_same_class function"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance
    of the specified class; otherwise False"""
    if type(obj) is not a_class:
        return False
    return True
