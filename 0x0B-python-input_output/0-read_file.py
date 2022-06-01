#!/usr/bin/python3
"""This module define the read_file function"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout
    Args:
    filename (str): filename
    """
    with open(filename, encoding="utf-8") as f:
        file = f.read()
        print(file, end="")
