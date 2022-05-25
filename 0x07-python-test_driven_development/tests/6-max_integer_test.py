#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for max_integer"""
    def test_module_doc(self):
        "Test for module docstring"
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_doc(self):
        "Test for function docstring"
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_positive_at_beginning(self):
        "Test for all positives and max at the beginning"
        self.assertEqual(max_integer([10, 2, 3, 4, 5]), 10)

    def test_positive_in_the_middle(self):
        "Test for all positives and max in the middle"
        self.assertEqual(max_integer([1, 2, 30, 4, 5]), 30)

    def test_positive_at_end(self):
        "Test for all positives and max at the end"
        self.assertEqual(max_integer([1, 2, 3, 4, 50]), 50)

    def test_one_negative(self):
        "Test for one negative"
        self.assertEqual(max_integer([1, 2, -3, 4, 5]), 5)

    def test_all_negative(self):
        "Test for all negatives"
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_one_element(self):
        "Test for one element"
        self.assertEqual(max_integer([10]), 10)

    def test_empty_list(self):
        "Test for empty list"
        self.assertIsNone(max_integer([]))

    def test_no_arg(self):
        "Test for no arguments pass to function"
        self.assertIsNone(max_integer())

    def test_none(self):
        "Test for None as argument"
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        "Test for non-integer argument"
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, "4", 5])
