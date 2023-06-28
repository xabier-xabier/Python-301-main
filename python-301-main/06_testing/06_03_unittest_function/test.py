import math
import unittest
import eq_function
import numpy as np


class TestEq(unittest.TestCase):

    def test_good_values(self):
        eq_function.Funcion.equation_func(2,2,1)

    def test_bad_values(self):
        eq_function.Funcion.equation_func(2,2,0)

class TestIq(unittest.TestCase):

    def test_check(self):
        self.assertEqual(eq_function.Funcion.equation_func(2,2,1),4.753580423112485)

    def test_wrong(self):
        self.assertEqual(eq_function.Funcion.equation_func(2,2,1),2)