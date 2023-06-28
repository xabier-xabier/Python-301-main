# Write two unittest test cases for the `subtract_divide()` function
# in `mymath.py`
#
# 1. Check for correct results by providing example input.
# 2. Check that a `CustomZeroDivisionError` gets raised correctly.
import mymath
import unittest

class TestMath(unittest.TestCase):
    def test_non_zero(self):
        mymath.subtract_divide(10,5,2)

    def test_zero_division(self):
        mymath.subtract_divide(10,5,5)