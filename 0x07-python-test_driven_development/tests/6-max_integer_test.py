#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unittest class in max_integer"""

    def testModule(self):
        """tests module docsting"""
        self.assertTrue(len(__import__('6-max_integer').__doc__) > 1)

    def testOneElem(self):
        """ test one element in method"""
        self.assertEqual(max_integer([5]), 5)
    
    def testMoreElem(self):
        """ test more element"""
        self.assertEqual(max_integer([1,5,3,2,9]), 9)
        self.assertEqual(max_integer([90,5,3,2,9]), 90)
        self.assertEqual(max_integer([1,5,13,2,9]), 13)
    
    def testAllElemNegative(self):
        """Tests for list with all negative numbers"""
        
        self.assertEqual(max_integer([-6, -50, -75, -100]), -6)

    def testString(self):
        """Test a string."""
        string = "zoo"
        self.assertEqual(max_integer(string), 'z')
    
    def testALLstr(self):
        """Test all list in string"""
        self.assertEqual(max_integer(["Car","Zoo","Bus"]), "Zoo")
    
    def testEmpty(self):
        """Test an empty , empty list and emmpty string"""
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(""), None)
    

 
if __name__ == '__main__':
    unittest.main()
    