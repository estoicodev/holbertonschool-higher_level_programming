#!/usr/bin/python3
"""This module defines a Base class"""


import json
from os import path


class Base:
    """class Base
    Attributes:
    id (int): Id of the instance"""
    __nb_objects = 0

    @staticmethod
    def reset_class():
        """Reset the attributes of the class for testing"""
        Base.__nb_objects = 0

    def __init__(self, id=None):
        """Initializes an instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        str_json = json.dumps(list_dictionaries)
        return str_json

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        list_dicts = []
        if list_objs is None:
            with open(f"{cls.__name__}.json", mode="w", encoding="utf-8") as f:
                f.write("[]")
            return
        for instance in list_objs:
            new_dict = instance.to_dictionary()
            list_dicts.append(new_dict)
        with open(f"{cls.__name__}.json", mode="w", encoding="utf-8") as f:
            text = Base.to_json_string(list_dicts)
            f.write(text)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
            dummy.update(**dictionary)
            return dummy
        elif cls.__name__ == "Square":
            dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        if not path.exists(f"{cls.__name__}.json"):
            return []
        with open(f"{cls.__name__}.json", encoding="utf-8") as f:
            text_json = f.read()
            obj_list = Base.from_json_string(text_json)

        list_instances = []
        for instance in obj_list:
            new_instance = cls.create(**instance)
            list_instances.append(new_instance)
        return list_instances
