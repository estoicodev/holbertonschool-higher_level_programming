#!/usr/bin/python3
"""This module defines the append_write function"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    Args:
    filename (str): filename
    text (str): text to append
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        n = f.write(text)
    return n
