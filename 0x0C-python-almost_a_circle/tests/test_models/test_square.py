"""Unittest for Square class"""

import unittest
import io
import contextlib
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
        """Testing for instance of Rectangle"""
        Square.reset_class()
        r = Square(1, 1)
        self.assertEqual(isinstance(r, Square), True)

    def test_no_args(self):
        """Testing for no args"""
        Square.reset_class()
        with self.assertRaises(TypeError) as e:
            r = Square()
        self.assertEqual(
            str(e.exception),
            "__init__() missing 1 required positional argument: 'size'")
