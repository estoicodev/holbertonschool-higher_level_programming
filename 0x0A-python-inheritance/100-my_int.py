#!/usr/bin/python3
"""This module defines a MyInt class inherited to int class"""


class MyInt(int):
    """MyInt class inherited to int class"""
    def __eq__(self, other):
        """
        Args:
        other (obj): other instance of class MyInt
        Returns:
        int: Boolean value. Returns True or False
        """
        return self.real != other.real

    def __ne__(self, other):
        """
        Args:
        other (obj): other instance of class MyInt
        Returns:
        int: Boolean value. Returns True or False
        """
        return self.real == other.real
