# Write a script that demonstrates TDD. Using pseudocode, plan out
# a couple of small functions. They could be as fundamental as adding
# and subtracting numbers with each other,
# or more complex such as functions that read and write to files.
#
# Instead of writing the functions, however, only write the tests for them.
# Think about how your functions might fail and write tests that will check 
# for that and identify these failures.
#
# You do not need to implement the actual functions after writing the tests 
# but of course you can do that, too.

import unittest
import tdd_approach

class TestFunc(unittest.TestCase):

    def test_first(self):
        fun=tdd_approach.Funcion_.add_numbers()
        self.assertEqual(len(fun),10)             #Check that the length is proper

    def test_delete(self):
        self.assertEqual(len(tdd_approach.Funcion_.delete_num(8,tdd_approach.Funcion_.add_numbers())),9) # Check that length has been reduced

    

    
