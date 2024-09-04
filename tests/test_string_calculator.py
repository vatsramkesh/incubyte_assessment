"""
Test cases to test string calculator
"""
import unittest

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