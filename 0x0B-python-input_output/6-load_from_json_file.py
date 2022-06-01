#!/usr/bin/python3
"""This module defines the load_from_json_file function"""


import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”
    Args:
    filename (str): filename
    """
    with open(filename, encoding="utf-8") as f:
        file = f.read()
        obj = json.loads(file)
    return obj
