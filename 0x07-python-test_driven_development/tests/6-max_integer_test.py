#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestMaxInteger Class.
    """
    def test_max(self):
        """Tests assertEqual."""
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([3, 2, 3]), 3)
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_max2(self):
        """Tests assetRaises and value None."""
        self.assertEqual(max_integer([]), None)
        self.assertRaises(TypeError, max_integer, [1, 'a'])
        self.assertRaises(TypeError, max_integer, ['a', 1])
