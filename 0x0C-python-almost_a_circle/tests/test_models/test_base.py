"""Unittest for Base class"""

import json
import os
from os import path
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """This class is an unittest for the Base class"""

    def test_single_instance_without_id(self):
        """Testing for single instance of Base class without id"""
        Base.reset_class()
        b = Base()
        self.assertEqual(b.id, 1)

    def test_multiple_instances_without_id(self):
        """Testing for multiple instances of Base class without id"""
        Base.reset_class()
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_single_instance_with_id(self):
        """Testing for single instance of Base class with id"""
        Base.reset_class()
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_multiple_instances_with_id(self):
        """Testing for multiple instances of Base class with id"""
        Base.reset_class()
        b1 = Base(10)
        b2 = Base(20)
        b3 = Base(30)
        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, 20)
        self.assertEqual(b3.id, 30)

    def test_duplicated_id(self):
        """Testing for duplicated id"""
        Base.reset_class()
        b1 = Base(10)
        b2 = Base(10)
        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, 10)

    def test_single_instance_with_None_id(self):
        """Testing for single instance of Base class with None id"""
        Base.reset_class()
        b = Base(None)
        self.assertEqual(b.id, 1)

    def test_multiple_instances_with_None_id(self):
        """Testing for multiple instances of Base class with None id"""
        Base.reset_class()
        b1 = Base(None)
        b2 = Base(None)
        b3 = Base(None)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_multiple_instances_with_id_and_without_id(self):
        """Testing for multiple instances of Base class with and without id"""
        Base.reset_class()
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, 3)

    def test_private_class_variable(self):
        """Testing for private Base class variable"""
        Base.reset_class()
        with self.assertRaises(AttributeError) as e:
            print(Base.__nb_objects)
        self.assertEqual(str(e.exception), "type object 'Base' has no attrib"
                                           "ute '_TestBaseClass__nb_objects'")

    def test_to_json_string(self):
        """Testing to_json_string method"""
        Base.reset_class()
        r = Rectangle(1, 2, 3, 4)
        new_dict = r.to_dictionary()
        json_dict = Base.to_json_string([new_dict])
        self.assertEqual(len(json_dict),
                         len('[{"id": 1, "width": 1, "height": 2, "x": 3, '
                             '"y": 4}]'))

    def test_to_json_string_with_None_arg(self):
        """Testing to_json_string method with None arg"""
        json_dict = Base.to_json_string(None)
        self.assertEqual(json_dict, "[]")
        self.assertEqual(type(json_dict), str)

    def test_to_json_string_with_empty_list(self):
        """Testing to_json_string method with empty list"""
        json_dict = Base.to_json_string([])
        self.assertEqual(json_dict, "[]")
        self.assertEqual(type(json_dict), str)

    def test_to_json_string_with_nan_arg(self):
        """Testing to_json_string method with NaN arg"""
        with self.assertRaises(TypeError) as e:
            Base.to_json_string(float("nan"))
        self.assertEqual(
            str(e.exception), "object of type 'float' has no len()")

    def test_to_json_string_with_inf_arg(self):
        """Testing to_json_string method with inf arg"""
        with self.assertRaises(TypeError) as e:
            Base.to_json_string(float("inf"))
        self.assertEqual(
            str(e.exception), "object of type 'float' has no len()")

    def test_save_to_file_Rectangle(self):
        """Testing save_to_file method with Rectangle class"""
        Base.reset_class()
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            text_file = file.read()
        self.assertEqual(
            len(text_file),
            len('[{"width": 10, "height": 7, "x": 2, "y": 8, "id": 1}, '
                '{"width": 2, "height": 4, "x": 0, "y": 0, "id": 2}]'))

    def test_save_to_file_Rectangle_with_None_arg(self):
        """Testing save_to_file method with Rectangle class with None arg"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            text_file = file.read()
        self.assertEqual(len(text_file), len("[]"))

    def test_save_to_file_Rectangle_with_empty_list(self):
        """Testing save_to_file method with Rectangle class with empty list"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            text_file = file.read()
        self.assertEqual(len(text_file), len("[]"))

    def test_save_to_file_Rectangle_overwrite_file(self):
        """Testing save_to_file method with Rectangle class with None arg"""
        Base.reset_class()
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        r3 = Rectangle(1, 1, 1)
        r4 = Rectangle(1, 1)
        Rectangle.save_to_file([r3, r4])
        with open("Rectangle.json", "r") as file:
            text_file = file.read()
        self.assertEqual(
            len(text_file),
            len('[{"width": 1, "height": 1, "x": 1, "y": 0, "id": 3}, '
                '{"width": 1, "height": 1, "x": 0, "y": 0, "id": 4}]'))

    def test_save_to_file_Square(self):
        """Testing save_to_file method with Square class"""
        Base.reset_class()
        r1 = Square(10, 7, 2)
        r2 = Square(2, 4)
        Square.save_to_file([r1, r2])
        with open("Square.json", "r") as file:
            text_file = file.read()
        self.assertEqual(
            len(text_file),
            len('[{"size": 10, "x": 7, "y": 2, "id": 1}, '
                '{"size": 2, "x": 4, "y": 0, "id": 2}]'))

    def test_save_to_file_Square_with_None_arg(self):
        """Testing save_to_file method with Square class with None arg"""
        os.remove("Square.json")
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            text_file = file.read()
        self.assertEqual(len(text_file), len("[]"))

    def test_save_to_file_Square_with_empty_list(self):
        """Testing save_to_file method with Square class with empty list"""
        os.remove("Square.json")
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            text_file = file.read()
        self.assertEqual(len(text_file), len("[]"))

    def test_save_to_file_Square_overwrite_file(self):
        """Testing save_to_file method with Square with None arg"""
        Base.reset_class()
        r1 = Square(10, 7, 2)
        r2 = Square(2, 4)
        Square.save_to_file([r1, r2])
        r3 = Square(1, 1, 1)
        r4 = Square(1, 1)
        Square.save_to_file([r3, r4])
        with open("Square.json", "r") as file:
            text_file = file.read()
        self.assertEqual(
            len(text_file),
            len('[{"size": 1, "x": 1, "y": 1, "id": 3}, '
                '{"size": 1, "x": 1, "y": 0, "id": 4}]'))

    def test_from_json_string_Rectangle(self):
        """Testing from_json_string method with Rectangle class"""
        Base.reset_class()
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output,
                         [{'id': 89, 'width': 10, 'height': 4},
                          {'id': 7, 'width': 1, 'height': 7}])
        self.assertEqual(type(list_output), list)

    def test_from_json_string_Rectangle_with_None_arg(self):
        """Testing from_json_string method with None arg"""
        list_output = Rectangle.from_json_string(None)
        self.assertEqual(list_output, [])
        self.assertEqual(type(list_output), list)

    def test_from_json_string_Rectangle_with_empty_list(self):
        """Testing from_json_string method with empty list"""
        Base.reset_class()
        list_output = Rectangle.from_json_string([])
        self.assertEqual(len(list_output), 0)
        self.assertEqual(type(list_output), list)

    def test_from_json_string_Square(self):
        """Testing from_json_string method with Square class"""
        Base.reset_class()
        list_input = [
            {'id': 89, 'size': 10, 'x': 4, 'y': 2},
            {'id': 7, 'size': 1, 'x': 7, 'y': 5}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_output,
                         [{'id': 89, 'size': 10, 'x': 4, 'y': 2},
                          {'id': 7, 'size': 1, 'x': 7, 'y': 5}])
        self.assertEqual(type(list_output), list)

    def test_from_json_string_Square_with_None_arg(self):
        """Testing from_json_string method with Square with None arg"""
        list_output = Square.from_json_string(None)
        self.assertEqual(list_output, [])
        self.assertEqual(type(list_output), list)

    def test_from_json_string_Square_with_empty_list(self):
        """Testing from_json_string method with Square with empty list"""
        Base.reset_class()
        list_output = Square.from_json_string([])
        self.assertEqual(len(list_output), 0)
        self.assertEqual(type(list_output), list)

    def test_create_Rectangle(self):
        """Testing create method with Rectangle class"""
        Base.reset_class()
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")
        self.assertIsNot(r2, r1)
        self.assertNotEqual(r2, r1)

    def test_create_Square(self):
        """Testing create method with Square class"""
        Base.reset_class()
        r1 = Square(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Square] (1) 5/1 - 3")
        self.assertEqual(str(r2), "[Square] (1) 5/1 - 3")
        self.assertIsNot(r2, r1)
        self.assertNotEqual(r2, r1)

    def test_load_from_file_Rectangle(self):
        """Testing load_from_file method for Rectangle class"""
        os.remove("Rectangle.json")
        Base.reset_class()
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_input[0]),
                         "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(str(list_rectangles_input[1]),
                         "[Rectangle] (2) 0/0 - 2/4")
        self.assertNotEqual(id(list_rectangles_input[0]),
                            id(list_rectangles_input[1]))
        self.assertEqual(str(list_rectangles_output[0]),
                         "[Rectangle] (1) 2/8 - 10/7")
        self.assertEqual(str(list_rectangles_output[1]),
                         "[Rectangle] (2) 0/0 - 2/4")
        self.assertNotEqual(id(list_rectangles_output[0]),
                            id(list_rectangles_output[1]))

    def test_load_from_file_Square(self):
        """Testing load_from_file method for Square class"""
        os.remove("Square.json")
        Base.reset_class()
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(list_squares_input[0]),
                         "[Square] (1) 0/0 - 5")
        self.assertEqual(str(list_squares_input[1]),
                         "[Square] (2) 9/1 - 7")
        self.assertNotEqual(id(list_squares_input[0]),
                            id(list_squares_input[1]))
        self.assertEqual(str(list_squares_input[0]),
                         "[Square] (1) 0/0 - 5")
        self.assertEqual(str(list_squares_output[1]),
                         "[Square] (2) 9/1 - 7")
        self.assertNotEqual(id(list_squares_output[0]),
                            id(list_squares_output[1]))
