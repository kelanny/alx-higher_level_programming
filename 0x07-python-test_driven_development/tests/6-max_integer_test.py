#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        # Test case 1: List with positive integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        # Test case 2: List with positive integers (unsorted)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

        # Test case 3: List with negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        # Test case 4: List with mixed positive and negative integers
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

        # Test case 5: List with one element
        self.assertEqual(max_integer([42]), 42)

        # Test case 6: List with empty input
        self.assertIsNone(max_integer([]))

        # Test case 7: List with duplicate maximum values
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

        # Test case 8: List with mixed types (should raise a TypeError)
        with self.assertRaises(TypeError):
            max_integer([1, 2, '3', 4])

if __name__ == '__main__':
    unittest.main()
