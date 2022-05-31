#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Inherited list class MyList for the print_sorted method."""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""

        print(sorted(self))
