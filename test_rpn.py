#!/usr/bin/env python3
import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        input("Press Enter to continue...")
        result = rpn.calculate("1 1 +")
        self.assertEqual(4, result)
        print("ran add")
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
        print("ran sub")
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
        print("ran mult")
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
        print("ran div")
    def test_exp(self):
        result = rpn.calculate("3 3 ^")
        self.assertEqual(27, result)
        print("ran exp")
