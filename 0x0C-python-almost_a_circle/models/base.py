"""This module defines a Base class"""
import csv
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
        """Writes the JSON string representation of list_objs to a json file"""
        list_dicts = []
        if list_objs is None or len(list_objs) == 0:
            with open(f"{cls.__name__}.json", mode="w", encoding="utf-8") as f:
                text = Base.to_json_string(list_dicts)
                f.write(text)
            return
        for instance in list_objs:
            new_dict = instance.to_dictionary()
            list_dicts.append(new_dict)
        with open(f"{cls.__name__}.json", mode="w", encoding="utf-8") as f:
            text = Base.to_json_string(list_dicts)
            f.write(text)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the csv string representation of list_objs to a csv file"""
        list_dicts = []
        if list_objs is None or len(list_objs) == 0:
            with open(f"{cls.__name__}.csv", mode="w", encoding="utf-8") as f:
                f.write("")
            return
        for instance in list_objs:
            new_dict = instance.to_dictionary()
            list_dicts.append(new_dict)
        with open(f"{cls.__name__}.csv", mode="w", encoding="utf-8") as f:
            if str(cls.__name__) == "Rectangle":
                keys = ["id", "width", "height", "x", "y"]
            elif str(cls.__name__) == "Square":
                keys = ["id", "size", "x", "y"]
            text = ""
            for i in range(len(list_dicts)):
                obj = list_dicts[i]
                for j in range(len(obj)):
                    key = keys[j]
                    if j != len(obj) - 1:
                        text += f"{obj[key]},"
                    else:
                        text += f"{obj[key]}"
                if i != len(list_dicts) - 1:
                    text += "\n"
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
        """Returns a list of instances from a json file"""
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

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances from a csv file"""
        if not path.exists(f"{cls.__name__}.csv"):
            return []
        with open(f"{cls.__name__}.csv", encoding="utf-8") as f:
            if str(cls.__name__) == "Rectangle":
                keys = ["id", "width", "height", "x", "y"]
            elif str(cls.__name__) == "Square":
                keys = ["id", "size", "x", "y"]
            reader = csv.DictReader(f, fieldnames=keys)
            list_instances = []
            for dict_instance in reader:
                for key, value in dict_instance.items():
                    dict_instance[key] = int(value)
                new_instance = cls.create(**dict_instance)
                list_instances.append(new_instance)
        return list_instances
