"""
Test cases to test string calculator
"""
import unittest

from src.exceptions import InvalidInputException
from src.string_calculator import add


class TestStringCalculator(unittest.TestCase):
    def test_add_with_empty_string(self):
        result = add("")
        self.assertEqual(result, 0)

    def test_add_with_single_number_string(self):
        result = add("5")
        self.assertEqual(result, 5)

    def test_add_with_multiple_number_string(self):
        result = add("1,5,2")
        self.assertEqual(result, 8)

    def test_add_with_new_line_between_numbers(self):
        result = add("1\n2,3")
        self.assertEqual(result, 6)

    def test_add_with_new_line_between_and_end_of_numbers(self):
        result = add("1\n2,3, 6\n")
        self.assertEqual(result, 12)

    def test_add_with_custom_delimeter(self):
        result = add("//;\n1;2;3")
        self.assertEqual(result, 6)

    def test_add_with_negative_numbers(self):
        self.assertRaises(InvalidInputException, add, "1,-2,3,-7")
