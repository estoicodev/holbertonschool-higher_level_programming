#!/usr/bin/python3
"""This module defines the write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of
    characters written
    Args:
    filename (str): filename
    text (str): text to write
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        n = f.write(text)
    return n
