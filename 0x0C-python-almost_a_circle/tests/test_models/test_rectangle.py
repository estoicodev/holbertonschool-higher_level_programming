"""Unittest for Rectangle class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
import contextlib
import os


class TestRectangleClass(unittest.TestCase):
    """This class is an unittest for the Rectangle class"""

    def test_inheritance_by_Base(self):
        """Testing for inheritance by Base"""
        Rectangle.reset_class()
        self.assertEqual(issubclass(Rectangle, Base), True)

    def test_is_instance_Rectangle(self):
        """Testing for instance of Rectangle"""
        Rectangle.reset_class()
        r = Rectangle(1, 1)
        self.assertEqual(isinstance(r, Rectangle), True)

    def test_no_args(self):
        """Testing for no args"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        self.assertEqual(
            str(e.exception),
            "__init__() missing 2 required positional arguments: 'width'"
            " and 'height'")

    def test_one_arg(self):
        """Testing for 1 arg"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1)
        self.assertEqual(
            str(e.exception),
            "__init__() missing 1 required positional argument: 'height'")

    def test_six_or_more_args(self):
        """Testing for six or more args"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 1, 1, 1, 1)
        self.assertEqual(
            str(e.exception),
            "__init__() takes from 3 to 6"
            " positional arguments but 7 were given")

    def test_single_instance(self):
        """Testing for single instance"""
        Rectangle.reset_class()
        r = Rectangle(2, 3)
        self.assertEqual(r.id, 1)

    def test_multiple_instances(self):
        """Testing for multiple instances"""
        Rectangle.reset_class()
        r1 = Rectangle(2, 3)
        r2 = Rectangle(4, 5)
        r3 = Rectangle(6, 7)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 3)

    def test_all_attributes(self):
        """Testing for all attributes complete"""
        Rectangle.reset_class()
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_duplicated_id(self):
        """Testing for duplicated id"""
        Rectangle.reset_class()
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.id, r2.id)

    def test_more_than_5_args(self):
        """Testing for more than 5 args"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, 4, 5, 6)
        self.assertEqual(
            str(e.exception),
            "__init__() takes from 3 to 6 positional "
            "arguments but 7 were given")

    def test_width_less_than_zero(self):
        """Testing for width less than zero"""
        Rectangle.reset_class()
        with self.assertRaises(ValueError) as e:
            r = Rectangle(-1, 1)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_width_equals_to_zero(self):
        """Testing for width equals to zero"""
        Rectangle.reset_class()
        with self.assertRaises(ValueError) as e:
            r = Rectangle(0, 1)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_height_less_than_zero(self):
        """Testing for height less than zero"""
        Rectangle.reset_class()
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, -1)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_height_equals_to_zero(self):
        """Testing for height equals to zero"""
        Rectangle.reset_class()
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 0)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_x_less_than_zero(self):
        """Testing for x less than zero"""
        Rectangle.reset_class()
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 1, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_y_less_than_zero(self):
        """Testing for y less than zero"""
        Rectangle.reset_class()
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 1, 1, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_width_str(self):
        """Testing for width str"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle("1", 1)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_width_float(self):
        """Testing for width float"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1.5, 1)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_width_bool(self):
        """Testing for width bool"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(True, 1)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_width_tuple(self):
        """Testing for width tuple"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle((1, 2), 1)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_width_list(self):
        """Testing for width list"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle([1, 2], 1)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_width_set(self):
        """Testing for width set"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle({1, 2}, 1)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_width_dict(self):
        """Testing for width dict"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle({"foo": 1}, 1)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_width_none(self):
        """Testing for width None"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(None, 1)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_width_funcs(self):
        """Testing for width funcs"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(print(), 1)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_width_nan(self):
        """Testing for width nan"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(float("nan"), 1)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_width_inf(self):
        """Testing for width inf"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(float("inf"), 1)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_height_str(self):
        """Testing for height str"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, "1")
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_height_float(self):
        """Testing for height float"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1.5)
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_height_bool(self):
        """Testing for height bool"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, True)
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_height_tuple(self):
        """Testing for height tuple"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, (1, 2))
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_height_list(self):
        """Testing for height list"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, [1, 2])
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_height_set(self):
        """Testing for height set"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, {1, 2})
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_height_dict(self):
        """Testing for height dict"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, {"foo": 1})
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_height_none(self):
        """Testing for height None"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, None)
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_height_funcs(self):
        """Testing for height funcs"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, print())
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_height_nan(self):
        """Testing for width nan"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, float("nan"))
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_height_inf(self):
        """Testing for height inf"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, float("inf"))
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_x_str(self):
        """Testing for x str"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, "1")
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_x_float(self):
        """Testing for x float"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 1.5)
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_x_bool(self):
        """Testing for x bool"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, True)
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_x_tuple(self):
        """Testing for x tuple"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, (1, 2))
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_x_list(self):
        """Testing for x list"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, [1, 2])
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_x_set(self):
        """Testing for x set"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, {1, 2})
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_x_dict(self):
        """Testing for x dict"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, {"foo": 1})
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_x_none(self):
        """Testing for x None"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, None)
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_x_funcs(self):
        """Testing for x funcs"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, print())
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_x_nan(self):
        """Testing for x nan"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, float("nan"))
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_x_inf(self):
        """Testing for x inf"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, float("inf"))
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_y_str(self):
        """Testing for y str"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 1, "1")
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_y_float(self):
        """Testing for y float"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 1, 1.5)
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_y_bool(self):
        """Testing for y bool"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 1, True)
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_y_tuple(self):
        """Testing for y tuple"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 1, (1, 2))
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_y_list(self):
        """Testing for y list"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 1, [1, 2])
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_y_set(self):
        """Testing for y set"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 1, {1, 2})
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_y_dict(self):
        """Testing for y dict"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 1, {"foo": 1})
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_y_none(self):
        """Testing for y None"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 1, None)
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_y_funcs(self):
        """Testing for y funcs"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 1, print())
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_y_nan(self):
        """Testing for y nan"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 1, float("nan"))
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_y_inf(self):
        """Testing for y inf"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 1, float("inf"))
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_no_id(self):
        """Testing for no id"""
        Rectangle.reset_class()
        r = Rectangle(1, 2)
        self.assertEqual(r.id, 1)

    def test_id_none(self):
        """Testing for id None"""
        Rectangle.reset_class()
        r = Rectangle(1, 2, 3, 4, None)
        self.assertEqual(r.id, 1)

    def test_width_getter(self):
        """Testing for width getter"""
        Rectangle.reset_class()
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)

    def test_height_getter(self):
        """Testing for height getter"""
        Rectangle.reset_class()
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.height, 2)

    def test_x_getter(self):
        """Testing for x getter"""
        Rectangle.reset_class()
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.x, 3)

    def test_y_getter(self):
        """Testing for y getter"""
        Rectangle.reset_class()
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.y, 4)

    def test_width_setter(self):
        """Testing for width setter"""
        Rectangle.reset_class()
        r = Rectangle(1, 2, 3, 4, 5)
        r.width = 10
        self.assertEqual(r.width, 10)

    def test_width_setter_validation_str(self):
        """Testing for width setter validation str"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, 4, 5)
            r.width = "foo"
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_width_setter_validation_equals_to_zero(self):
        """Testing for width setter validation equals to zero"""
        Rectangle.reset_class()
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, 3, 4, 5)
            r.width = 0
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_width_setter_validation_negative(self):
        """Testing for width setter validation less than zero"""
        Rectangle.reset_class()
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, 3, 4, 5)
            r.width = -1
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_height_setter(self):
        """Testing for height setter"""
        Rectangle.reset_class()
        r = Rectangle(1, 2, 3, 4, 5)
        r.height = 20
        self.assertEqual(r.height, 20)

    def test_height_setter_validation_str(self):
        """Testing for height setter validation str"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, 4, 5)
            r.height = "foo"
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_height_setter_validation_equals_to_zero(self):
        """Testing for height setter validation equals to zero"""
        Rectangle.reset_class()
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, 3, 4, 5)
            r.height = 0
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_height_setter_validation_negative(self):
        """Testing for height setter validation less than zero"""
        Rectangle.reset_class()
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, 3, 4, 5)
            r.height = -1
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_x_setter(self):
        """Testing for x setter"""
        Rectangle.reset_class()
        r = Rectangle(1, 2, 3, 4, 5)
        r.x = 30
        self.assertEqual(r.x, 30)

    def test_x_setter_validation_str(self):
        """Testing for x setter validation str"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, 4, 5)
            r.x = "foo"
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_x_setter_validation_negative(self):
        """Testing for x setter validation less than zero"""
        Rectangle.reset_class()
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, 3, 4, 5)
            r.x = -1
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_y_setter(self):
        """Testing for y setter"""
        Rectangle.reset_class()
        r = Rectangle(1, 2, 3, 4, 5)
        r.y = 40
        self.assertEqual(r.y, 40)

    def test_y_setter_validation_str(self):
        """Testing for x setter validation str"""
        Rectangle.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, 4, 5)
            r.y = "foo"
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_y_setter_validation_negative(self):
        """Testing for y setter validation less than zero"""
        Rectangle.reset_class()
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, 3, 4, 5)
            r.y = -1
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_private_class_variable(self):
        """Testing for private class variable"""
        Rectangle.reset_class()
        with self.assertRaises(AttributeError) as e:
            print(Rectangle.__nb_objects)
        self.assertEqual(
            str(e.exception),
            "type object \'Rectangle\' has no attribute "
            "\'_TestRectangleClass__nb_objects\'")

    def test_private_width_variable(self):
        """Testing for private width variable"""
        Rectangle.reset_class()
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(AttributeError) as e:
            print(r.__width)
        self.assertEqual(
            str(e.exception),
            "\'Rectangle\' object has no attribute "
            "\'_TestRectangleClass__width\'")

    def test_private_height_variable(self):
        """Testing for private height variable"""
        Rectangle.reset_class()
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(AttributeError) as e:
            print(r.__height)
        self.assertEqual(
            str(e.exception),
            "\'Rectangle\' object has no attribute "
            "\'_TestRectangleClass__height\'")

    def test_private_x_variable(self):
        """Testing for private x variable"""
        Rectangle.reset_class()
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(AttributeError) as e:
            print(r.__x)
        self.assertEqual(
            str(e.exception),
            "\'Rectangle\' object has no attribute "
            "\'_TestRectangleClass__x\'")

    def test_private_y_variable(self):
        """Testing for private y variable"""
        Rectangle.reset_class()
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(AttributeError) as e:
            print(r.__y)
        self.assertEqual(
            str(e.exception),
            "\'Rectangle\' object has no attribute "
            "\'_TestRectangleClass__y\'")

    def test_public_area_method(self):
        """Testing for public area method"""
        Rectangle.reset_class()
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_public_area_method_with_arg(self):
        """Testing for public area method with arg"""
        Rectangle.reset_class()
        r = Rectangle(5, 10)
        with self.assertRaises(TypeError) as e:
            r.area(10)
        self.assertEqual(
            str(e.exception),
            "area() takes 1 positional argument but 2 were given")

    def test_public_update_method_id_attr(self):
        """Testing for public update method id attribute"""
        Rectangle.reset_class()
        r = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(r.id, 2)
        r.update(10)
        self.assertEqual(r.id, 10)

    def test_public_update_method_width_attr(self):
        """Testing for public update method width attribute"""
        Rectangle.reset_class()
        r = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(r.width, 2)
        r.update(10, 20)
        self.assertEqual(r.width, 20)

    def test_public_update_method_height_attr(self):
        """Testing for public update method height attribute"""
        Rectangle.reset_class()
        r = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(r.height, 2)
        r.update(10, 20, 30)
        self.assertEqual(r.height, 30)

    def test_public_update_method_x_attr(self):
        """Testing for public update method x attribute"""
        Rectangle.reset_class()
        r = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(r.x, 2)
        r.update(10, 20, 30, 40)
        self.assertEqual(r.x, 40)

    def test_public_update_method_y_attr(self):
        """Testing for public update method y attribute"""
        Rectangle.reset_class()
        r = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(r.y, 2)
        r.update(10, 20, 30, 40, 50)
        self.assertEqual(r.y, 50)

    def test_public_update_method_all_attrs(self):
        """Testing for public update method all attributes"""
        Rectangle.reset_class()
        r = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)
        r.update(10, 20, 30, 40, 50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_public_update_method_no_args(self):
        """Testing for public update method no args"""
        Rectangle.reset_class()
        r = Rectangle(2, 2, 2, 2, 2)
        r.update()
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)

    def test_public_update_method_width_attr_validation(self):
        """Testing for public update method width attribute validation"""
        Rectangle.reset_class()
        r = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(r.width, 2)
        with self.assertRaises(TypeError) as e:
            r.update(10, "foo")
        self.assertEqual(
            str(e.exception),
            "width must be an integer")

    def test_public_update_method_height_attr_validation(self):
        """Testing for public update method height attribute validation"""
        Rectangle.reset_class()
        r = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(r.height, 2)
        with self.assertRaises(TypeError) as e:
            r.update(10, 20, "foo")
        self.assertEqual(
            str(e.exception),
            "height must be an integer")

    def test_public_update_method_x_attr_validation(self):
        """Testing for public update method x attribute validation"""
        Rectangle.reset_class()
        r = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(r.x, 2)
        with self.assertRaises(TypeError) as e:
            r.update(10, 20, 30, "foo")
        self.assertEqual(
            str(e.exception),
            "x must be an integer")

    def test_public_update_method_y_attr_validation(self):
        """Testing for public update method y attribute validation"""
        Rectangle.reset_class()
        r = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(r.y, 2)
        with self.assertRaises(TypeError) as e:
            r.update(10, 20, 30, 40, "foo")
        self.assertEqual(
            str(e.exception),
            "y must be an integer")

    def test_public_update_method_kwargs_id(self):
        """Testing for public update method kwargs id attribute"""
        Rectangle.reset_class()
        r = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(r.id, 2)
        r.update(id=5)
        self.assertEqual(r.id, 5)

    def test_public_update_method_kwargs_width(self):
        """Testing for public update method kwargs width attribute"""
        Rectangle.reset_class()
        r = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(r.width, 2)
        r.update(width=10)
        self.assertEqual(r.width, 10)

    def test_public_update_method_kwargs_height(self):
        """Testing for public update method kwargs height attribute"""
        Rectangle.reset_class()
        r = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(r.height, 2)
        r.update(height=20)
        self.assertEqual(r.height, 20)

    def test_public_update_method_kwargs_x(self):
        """Testing for public update method kwargs x attribute"""
        Rectangle.reset_class()
        r = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(r.x, 2)
        r.update(x=30)
        self.assertEqual(r.x, 30)

    def test_public_update_method_kwargs_y(self):
        """Testing for public update method kwargs y attribute"""
        Rectangle.reset_class()
        r = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(r.y, 2)
        r.update(y=40)
        self.assertEqual(r.y, 40)

    def test_public_update_method_all_kwargs(self):
        """Testing for public update method all attributes kwargs"""
        Rectangle.reset_class()
        r = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 2)
        r.update(width=10, height=20, x=30, y=40, id=50)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 30)
        self.assertEqual(r.y, 40)
        self.assertEqual(r.id, 50)

    def test_public_update_method_kwargs_skipped(self):
        """Testing for public update method kwargs skipped"""
        Rectangle.reset_class()
        r = Rectangle(2, 2, 2, 2, 2)
        r.update(10, 20, 30, 40, width=5)
        self.assertEqual(r.id, 10)

    def test_public_update_method_kwargs_ignore_validation(self):
        """Testing for public update method kwargs skipped"""
        Rectangle.reset_class()
        r = Rectangle(2, 2, 2, 2, 2)
        r.update(10, 20, 30, 40, foo=5)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 2)

    def test_to_dictionary_method(self):
        """Testing for public to_dictionary method"""
        Rectangle.reset_class()
        r = Rectangle(10, 20, 2, 4)
        r_dict = r.to_dictionary()
        self.assertEqual(
            r_dict,
            {'width': 10, 'height': 20, 'x': 2, 'y': 4, 'id': 1})
        self.assertEqual(type(r_dict), dict)

    def test_update_with_dict(self):
        """Testing for update method with dictionary"""
        Rectangle.reset_class()
        r1 = Rectangle(10, 20, 2, 4)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle(5, 2)
        r2.update(**r1_dict)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 20)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 4)

    def test_str_method(self):
        """Testing for __str__ method"""
        Rectangle.reset_class()
        r1 = Rectangle(10, 20, 2, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (5) 2/4 - 10/20")
        r2 = Rectangle(4, 5)
        self.assertEqual(str(r2), "[Rectangle] (1) 0/0 - 4/5")

    def test_display_method(self):
        """Testing for display method validation 1"""
        Rectangle.reset_class()
        r1 = Rectangle(2, 3, 1, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r1.display()
        self.assertEqual(
            f.getvalue(),
            "\n\n ##\n ##\n ##\n")

    def test_display_method_2(self):
        """Testing for display method validation 2"""
        Rectangle.reset_class()
        r2 = Rectangle(4, 3, 0, 1)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r2.display()
        self.assertEqual(
            f.getvalue(),
            "\n####\n####\n####\n")

    def test_save_to_file_rectangle(self):
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

    def test_save_to_file_rectangle_with_None_arg(self):
        """Testing save_to_file method with Rectangle class with None arg"""
        os.remove("Rectangle.json")
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            text_file = file.read()
        self.assertEqual(text_file, "[]")

    def test_save_to_file_rectangle_with_empty_list(self):
        """Testing save_to_file method with Rectangle class with empty list"""
        os.remove("Rectangle.json")
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            text_file = file.read()
        self.assertEqual(text_file, "[]")

    def test_save_to_file_rectangle_overwrite_file(self):
        """Testing save_to_file method with Rectangle class with None arg"""
        os.remove("Rectangle.json")
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
