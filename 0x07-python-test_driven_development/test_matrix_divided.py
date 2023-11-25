import unittest
add_integer = __import__('2-matrix_divided.py').matrix_divided

class test_add_integer(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add_integer(1, 2), 3)
        res = add_integer(2, -3)
        self.assertEqual(res, -1)
        self.assertEqual(add_integer(999999999999999999999999999999, 1), 1000000000000000000000000000000)
        # add_integer(4, "School")
        self.assertRaises(TypeError, add_integer, "hello", 4)
        self.assertRaises(TypeError, add_integer, 4,  "School")
        self.assertRaises(TypeError, add_integer, "a", "4")

 
if __name__ == '__main__':
    unittest.main()
    