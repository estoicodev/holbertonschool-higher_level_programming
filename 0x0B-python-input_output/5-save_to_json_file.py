#!/usr/bin/python3
"""This module defines the save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation
    Args:
    my_obj (obj): Object to write into filename
    filename (str): filename
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        text = json.dumps(my_obj)
        f.write(text)
