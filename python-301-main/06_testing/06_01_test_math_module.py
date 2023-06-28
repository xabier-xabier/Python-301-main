# Write a unittest test suite with at least two methods that test
# the functionality of the built-in `math` module.

import math
import unittest

class TestMath(unittest.TestCase):
    def test_floor_rounds_down(self):
        self.assertEqual(math.floor(3.4), 3)

    def test_finite(self):
        self.assertEqual(math.isqrt(10),3)

