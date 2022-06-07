"""Unittest for Square class"""

import unittest
import io
import contextlib
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """This class is an unittest for the Square class"""

    def test_inheritance_by_Rectangle(self):
        """Testing for inheritance by Rectangle"""
        Square.reset_class()
        self.assertEqual(issubclass(Square, Rectangle), True)

    def test_is_instance_Square(self):
        """Testing for instance of Square"""
        Square.reset_class()
        self.assertIsInstance(Square(1), Square)

    def test_no_args(self):
        """Testing for no args"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Square()
        self.assertEqual(
            str(e.exception),
            "__init__() missing 1 required positional argument: 'size'")

    def test_one_arg(self):
        """Testing for one arg"""
        Square.reset_class()
        r = Square(1)
        self.assertEqual(r.size, 1)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_two_args(self):
        """Testing for two args"""
        Square.reset_class()
        r = Square(1, 2)
        self.assertEqual(r.size, 1)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_three_args(self):
        """Testing for three args"""
        Square.reset_class()
        r = Square(1, 2, 3)
        self.assertEqual(r.size, 1)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 1)

    def test_all_args(self):
        """Testing for four args"""
        Square.reset_class()
        r = Square(1, 2, 3, 4)
        self.assertEqual(r.size, 1)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 4)

    def test_five_or_more_args(self):
        """Testing for five or more args"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            Square(1, 2, 3, 4, 5)

    def test_single_instance(self):
        """Testing for single instance"""
        Square.reset_class()
        r = Square(1, 2, 3, 4)
        self.assertEqual(r.id, 4)

    def test_duplicated_id(self):
        """Testing for duplicated id"""
        Square.reset_class()
        r1 = Square(1, 2, 3, 4)
        r2 = Square(1, 2, 3, 4)
        self.assertEqual(r1.id, r2.id)

    def test_multiple_instances(self):
        """Testing for multiple instances"""
        Square.reset_class()
        r1 = Square(1, 2, 3, 4)
        r2 = Square(2, 3, 4, 5)
        r3 = Square(5, 6, 7, 8)
        self.assertEqual(r1.id, 4)
        self.assertEqual(r2.id, 5)
        self.assertEqual(r3.id, 8)

    def test_size_getter(self):
        """Testing for attribute size is private"""
        Square.reset_class()
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.size, 1)

    def test_width_getter(self):
        """Testing for attribute width is private"""
        Square.reset_class()
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.width, 1)

    def test_height_getter(self):
        """Testing for attribute height is private"""
        Square.reset_class()
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.height, 1)

    def test_x_getter(self):
        """Testing for attribute x is private"""
        Square.reset_class()
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.x, 2)

    def test_x_getter_zero(self):
        """Testing for attribute x is private"""
        Square.reset_class()
        s = Square(1)
        self.assertEqual(s.x, 0)

    def test_y_getter(self):
        """Testing for attribute y is private"""
        Square.reset_class()
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.y, 3)

    def test_y_getter_zero(self):
        """Testing for attribute y is private"""
        Square.reset_class()
        s = Square(1)
        self.assertEqual(s.y, 0)

    def test_size_setter(self):
        """Testing for set attribute size"""
        Square.reset_class()
        s = Square(1, 2, 3, 4)
        s.size = 10
        self.assertEqual(s.size, 10)

    def test_x_setter(self):
        """Testing for set attribute x"""
        Square.reset_class()
        s = Square(1, 2, 3, 4)
        s.x = 20
        self.assertEqual(s.x, 20)

    def test_y_setter(self):
        """Testing for set attribute y"""
        Square.reset_class()
        s = Square(1, 2, 3, 4)
        s.y = 30
        self.assertEqual(s.y, 30)

    def test_size_zero_validation(self):
        """Testing for size value validation"""
        Square.reset_class()
        with self.assertRaises(ValueError) as e:
            s = Square(0)
        self.assertEqual(
            str(e.exception),
            "width must be > 0")

    def test_size_less_than_zero_validation(self):
        """Testing for less than zero validation"""
        Square.reset_class()
        with self.assertRaises(ValueError) as e:
            s = Square(-1)
        self.assertEqual(
            str(e.exception),
            "width must be > 0")

    def test_size_validation_str(self):
        """Testing for size validation str"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square("foo")
        self.assertEqual(
            str(e.exception),
            "width must be an integer")

    def test_size_validation_bool(self):
        """Testing for size validation bool"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(True)
        self.assertEqual(
            str(e.exception),
            "width must be an integer")

    def test_size_validation_list(self):
        """Testing for size validation list"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square([1, 2])
        self.assertEqual(
            str(e.exception),
            "width must be an integer")

    def test_size_validation_tuple(self):
        """Testing for size validation tuple"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square((1, 2))
        self.assertEqual(
            str(e.exception),
            "width must be an integer")

    def test_size_validation_float(self):
        """Testing for size validation float"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1.5)
        self.assertEqual(
            str(e.exception),
            "width must be an integer")

    def test_size_validation_set(self):
        """Testing for size validation set"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square({1, 2})
        self.assertEqual(
            str(e.exception),
            "width must be an integer")

    def test_size_validation_dict(self):
        """Testing for size validation dict"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square({"foo": 1})
        self.assertEqual(
            str(e.exception),
            "width must be an integer")

    def test_size_validation_none(self):
        """Testing for size validation None"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(None)
        self.assertEqual(
            str(e.exception),
            "width must be an integer")

    def test_size_validation_complex(self):
        """Testing for size validation complex number"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(complex(5))
        self.assertEqual(
            str(e.exception),
            "width must be an integer")

    def test_size_validation_nan(self):
        """Testing for size validation nan"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(float("nan"))
        self.assertEqual(
            str(e.exception),
            "width must be an integer")

    def test_size_validation_inf(self):
        """Testing for size validation inf"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(float("inf"))
        self.assertEqual(
            str(e.exception),
            "width must be an integer")

    def test_size_validation_frozenset(self):
        """Testing for size validation frozenset"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(frozenset({1, 2, 3, 4}))
        self.assertEqual(
            str(e.exception),
            "width must be an integer")

    def test_size_validation_range(self):
        """Testing for size validation range"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(range(4))
        self.assertEqual(
            str(e.exception),
            "width must be an integer")

    def test_size_validation_byte(self):
        """Testing for size validation byte"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(b'Py')
        self.assertEqual(
            str(e.exception),
            "width must be an integer")

    def test_size_validation_bytearray(self):
        """Testing for size validation bytearray"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(bytearray(b'Py'))
        self.assertEqual(
            str(e.exception),
            "width must be an integer")

    def test_size_validation_memoryview(self):
        """Testing for size validation memoryview"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(memoryview(b'abcd'))
        self.assertEqual(
            str(e.exception),
            "width must be an integer")

    def test_x_less_than_zero_validation(self):
        """Testing for x less than zero"""
        Square.reset_class()
        with self.assertRaises(ValueError) as e:
            s = Square(1, -1)
        self.assertEqual(
            str(e.exception),
            "x must be >= 0")


    def test_x_validation_str(self):
        """Testing for x validation str"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, "foo")
        self.assertEqual(
            str(e.exception),
            "x must be an integer")


    def test_x_validation_bool(self):
        """Testing for size validation bool"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, True)
        self.assertEqual(
            str(e.exception),
            "x must be an integer")


    def test_x_validation_list(self):
        """Testing for x validation list"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, [1, 2])
        self.assertEqual(
            str(e.exception),
            "x must be an integer")


    def test_x_validation_tuple(self):
        """Testing for x validation tuple"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, (1, 2))
        self.assertEqual(
            str(e.exception),
            "x must be an integer")


    def test_x_validation_float(self):
        """Testing for x validation float"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, 1.5)
        self.assertEqual(
            str(e.exception),
            "x must be an integer")


    def test_x_validation_set(self):
        """Testing for x validation set"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, {1, 2})
        self.assertEqual(
            str(e.exception),
            "x must be an integer")


    def test_x_validation_dict(self):
        """Testing for x validation dict"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, {"foo": 1})
        self.assertEqual(
            str(e.exception),
            "x must be an integer")


    def test_x_validation_none(self):
        """Testing for x validation None"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, None)
        self.assertEqual(
            str(e.exception),
            "x must be an integer")


    def test_x_validation_complex(self):
        """Testing for x validation complex number"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, complex(5))
        self.assertEqual(
            str(e.exception),
            "x must be an integer")


    def test_x_validation_nan(self):
        """Testing for x validation nan"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, float("nan"))
        self.assertEqual(
            str(e.exception),
            "x must be an integer")


    def test_x_validation_inf(self):
        """Testing for x validation inf"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, float("inf"))
        self.assertEqual(
            str(e.exception),
            "x must be an integer")


    def test_x_validation_frozenset(self):
        """Testing for x validation frozenset"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, frozenset({1, 2, 3, 4}))
        self.assertEqual(
            str(e.exception),
            "x must be an integer")


    def test_x_validation_range(self):
        """Testing for x validation range"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, range(4))
        self.assertEqual(
            str(e.exception),
            "x must be an integer")


    def test_x_validation_byte(self):
        """Testing for x validation byte"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, b'Py')
        self.assertEqual(
            str(e.exception),
            "x must be an integer")


    def test_x_validation_bytearray(self):
        """Testing for x validation bytearray"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, bytearray(b'Py'))
        self.assertEqual(
            str(e.exception),
            "x must be an integer")


    def test_x_validation_memoryview(self):
        """Testing for x validation memoryview"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, memoryview(b'abcd'))
        self.assertEqual(
            str(e.exception),
            "x must be an integer")

    def test_y_less_than_zero_validation(self):
        """Testing for y less than zero"""
        Square.reset_class()
        with self.assertRaises(ValueError) as e:
            s = Square(1, 1, -1)
        self.assertEqual(
            str(e.exception),
            "y must be >= 0")


    def test_y_validation_str(self):
        """Testing for y validation str"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, 1, "foo")
        self.assertEqual(
            str(e.exception),
            "y must be an integer")


    def test_y_validation_bool(self):
        """Testing for y validation bool"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, 1, True)
        self.assertEqual(
            str(e.exception),
            "y must be an integer")


    def test_y_validation_list(self):
        """Testing for y validation list"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, 1, [1, 2])
        self.assertEqual(
            str(e.exception),
            "y must be an integer")


    def test_y_validation_tuple(self):
        """Testing for y validation tuple"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, 1, (1, 2))
        self.assertEqual(
            str(e.exception),
            "y must be an integer")


    def test_y_validation_float(self):
        """Testing for y validation float"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, 1, 1.5)
        self.assertEqual(
            str(e.exception),
            "y must be an integer")


    def test_y_validation_set(self):
        """Testing for y validation set"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, 1, {1, 2})
        self.assertEqual(
            str(e.exception),
            "y must be an integer")


    def test_y_validation_dict(self):
        """Testing for y validation dict"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, 1, {"foo": 1})
        self.assertEqual(
            str(e.exception),
            "y must be an integer")


    def test_y_validation_none(self):
        """Testing for y validation None"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, 1, None)
        self.assertEqual(
            str(e.exception),
            "y must be an integer")


    def test_y_validation_complex(self):
        """Testing for y validation complex number"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, 1, complex(5))
        self.assertEqual(
            str(e.exception),
            "y must be an integer")


    def test_y_validation_nan(self):
        """Testing for y validation nan"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, 1, float("nan"))
        self.assertEqual(
            str(e.exception),
            "y must be an integer")


    def test_y_validation_inf(self):
        """Testing for y validation inf"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, 1, float("inf"))
        self.assertEqual(
            str(e.exception),
            "y must be an integer")


    def test_y_validation_frozenset(self):
        """Testing for y validation frozenset"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, 1, frozenset({1, 2, 3, 4}))
        self.assertEqual(
            str(e.exception),
            "y must be an integer")


    def test_y_validation_range(self):
        """Testing for y validation range"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, 1, range(4))
        self.assertEqual(
            str(e.exception),
            "y must be an integer")


    def test_y_validation_byte(self):
        """Testing for y validation byte"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, 1, b'Py')
        self.assertEqual(
            str(e.exception),
            "y must be an integer")


    def test_y_validation_bytearray(self):
        """Testing for y validation bytearray"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, 1, bytearray(b'Py'))
        self.assertEqual(
            str(e.exception),
            "y must be an integer")


    def test_y_validation_memoryview(self):
        """Testing for y validation memoryview"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            s = Square(1, 1, memoryview(b'abcd'))
        self.assertEqual(
            str(e.exception),
            "y must be an integer")

    def test_area_method_small(self):
        """Testing for area method small size"""
        Square.reset_class()
        self.assertEqual(Square(10).area(), 100)

    def test_area_method_large(self):
        """Testing for area method large size"""
        Square.reset_class()
        s = Square(999999999999999999)
        self.assertEqual(s.area(), 999999999999999998000000000000000001)

    def test_area_method_change_size(self):
        """Testing for area method resizing"""
        Square.reset_class()
        s = Square(4)
        s.size = 6
        self.assertEqual(s.area(), 36)

    def test_area_method_one_arg(self):
        """Testing for area method with arg"""
        Square.reset_class()
        s = Square(4)
        with self.assertRaises(TypeError) as e:
            s.area(10)

    def test_str_method_one_attr(self):
        """Testing for __str__ method with set one attribute of the instance"""
        Square.reset_class()
        s = Square(4)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 4")

    def test_str_method_two_attr(self):
        """Testing for __str__ method with set two attributes of the instance"""
        Square.reset_class()
        s = Square(4, 2)
        self.assertEqual(str(s), "[Square] (1) 2/0 - 4")

    def test_str_method_three_attr(self):
        """Testing for __str__ method with set three attributes of the instance"""
        Square.reset_class()
        s = Square(4, 2, 3)
        self.assertEqual(str(s), "[Square] (1) 2/3 - 4")

    def test_str_method_all_attr(self):
        """Testing for __str__ method with set all attributes of the instance"""
        Square.reset_class()
        s = Square(4, 2, 3, 5)
        self.assertEqual(str(s), "[Square] (5) 2/3 - 4")

    def test_str_method_one_arg(self):
        """Testing for __str__ method with one arg"""
        Square.reset_class()
        s = Square(4, 2, 3, 5)
        with self.assertRaises(TypeError) as e:
            s.__str__(10)

    def test_display_method_one_attr(self):
        """Testing for display method with set one attribute of the instance"""
        Square.reset_class()
        s1 = Square(4)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            s1.display()
        self.assertEqual(
            f.getvalue(),
            "####\n####\n####\n####\n")

    def test_display_method_two_attr(self):
        """Testing for display method with set two attributes of the instance"""
        Square.reset_class()
        s1 = Square(4, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            s1.display()
        self.assertEqual(
            f.getvalue(),
            "  ####\n  ####\n  ####\n  ####\n")

    def test_display_method_three_attr(self):
        """Testing for display method with set three attributes of the instance"""
        Square.reset_class()
        s1 = Square(4, 2, 1)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            s1.display()
        self.assertEqual(
            f.getvalue(),
            "\n  ####\n  ####\n  ####\n  ####\n")

    def test_display_method_x_attr_zero(self):
        """Testing for display method with set zero to x attribute"""
        Square.reset_class()
        s1 = Square(4, 0, 1)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            s1.display()
        self.assertEqual(
            f.getvalue(),
            "\n####\n####\n####\n####\n")

    def test_display_method_y_attr_zero(self):
        """Testing for display method with set zero to y attribute"""
        Square.reset_class()
        s1 = Square(4, 2, 0)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            s1.display()
        self.assertEqual(
            f.getvalue(),
            "  ####\n  ####\n  ####\n  ####\n")

    def test_display_method_one_arg(self):
        """Testing for display method with one arg"""
        Square.reset_class()
        s1 = Square(4, 2, 1)
        with self.assertRaises(TypeError) as e:
            s1.display(10)

    def test_update_no_arg(self):
        """Testing update id attribute with update method"""
        Square.reset_class()
        s = Square(2, 2, 2, 2)
        s.update()
        self.assertEqual(
            str(s),
            "[Square] (2) 2/2 - 2")

    def test_update_one_arg(self):
        """Testing update id attribute with update method"""
        Square.reset_class()
        s = Square(2, 2, 2, 2)
        self.assertEqual(s.id, 2)
        s.update(10)
        self.assertEqual(s.id, 10)

    def test_update_two_args(self):
        """Testing update size attribute with update method"""
        Square.reset_class()
        s = Square(2, 2, 2, 2)
        self.assertEqual(s.size, 2)
        s.update(10, 20)
        self.assertEqual(s.size, 20)

    def test_update_three_args(self):
        """Testing update x attribute with update method"""
        Square.reset_class()
        s = Square(2, 2, 2, 2)
        self.assertEqual(s.x, 2)
        s.update(10, 20, 30)
        self.assertEqual(s.x, 30)

    def test_update_four_args(self):
        """Testing update y attribute with update method"""
        Square.reset_class()
        s = Square(2, 2, 2, 2)
        self.assertEqual(s.y, 2)
        s.update(10, 20, 30, 40)
        self.assertEqual(s.y, 40)

    def test_update_all_args(self):
        """Testing update all attributes with update method"""
        Square.reset_class()
        s = Square(2, 2, 2, 2)
        self.assertEqual(s.y, 2)
        s.update(10, 20, 30, 40)
        self.assertEqual(
            str(s),
            "[Square] (10) 30/40 - 20")

    def test_update_kwargs_one(self):
        """Testing update with one kwargs with update method"""
        Square.reset_class()
        s = Square(2, 2, 2, 2)
        s.update(size=10)
        self.assertEqual(
            str(s),
            "[Square] (2) 2/2 - 10")

    def test_update_kwargs_two(self):
        """Testing update with two kwargs with update method"""
        Square.reset_class()
        s = Square(2, 2, 2, 2)
        s.update(size=10, x=5)
        self.assertEqual(
            str(s),
            "[Square] (2) 5/2 - 10")

    def test_update_kwargs_three(self):
        """Testing update with three kwargs with update method"""
        Square.reset_class()
        s = Square(2, 2, 2, 2)
        s.update(id=1, size=10, x=5)
        self.assertEqual(
            str(s),
            "[Square] (1) 5/2 - 10")

    def test_update_kwargs_four(self):
        """Testing update with four kwargs with update method"""
        Square.reset_class()
        s = Square(2, 2, 2, 2)
        s.update(id=1, size=10, x=5, y=3)
        self.assertEqual(
            str(s),
            "[Square] (1) 5/3 - 10")

    def test_update_kwargs_width_getter(self):
        """Testing update with kwargs width getter with update method"""
        Square.reset_class()
        s = Square(2, 2, 2, 2)
        s.update(id=1, size=8)
        self.assertEqual(s.width, 8)

    def test_update_kwargs_height_getter(self):
        """Testing update with kwargs height getter with update method"""
        Square.reset_class()
        s = Square(2, 2, 2, 2)
        s.update(id=1, size=9)
        self.assertEqual(s.height, 9)

    def test_to_dictionary(self):
        s1 = Square(1, 2, 3, 4)
        correct_dict = {'id': 4, 'size': 1, 'x': 2, 'y': 3}
        self.assertDictEqual(s1.to_dictionary(), correct_dict)

    def test_to_dictionary_with_arg(self):
        s1 = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            s1_dict = s1.to_dictionary(10)

    def test_save_to_file_square(self):
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

    def test_save_to_file_square_with_None_arg(self):
        """Testing save_to_file method with Square class with None arg"""
        os.remove("Square.json")
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            text_file = file.read()
        self.assertEqual(text_file, "[]")

    def test_save_to_file_square_with_empty_list(self):
        """Testing save_to_file method with Square class with empty list"""
        os.remove("Square.json")
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            text_file = file.read()
        self.assertEqual(text_file, "[]")

    def test_save_to_file_square_overwrite_file(self):
        """Testing save_to_file method with Square with None arg"""
        os.remove("Square.json")
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
