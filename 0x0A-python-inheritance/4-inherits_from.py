#!/usr/bin/python3
"""This module defines inherits_from function"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False"""
    if not issubclass(obj, a_class):
        return False
    return True
