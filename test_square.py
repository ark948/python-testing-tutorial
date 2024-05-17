import unittest
from square import Square

class TestSquare(unittest.TestCase):
    def test_area(self):
        square = Square(10)
        area = square.area()
        self.assertEqual(area, 100)

    def test_length_with_wrong_type(self):
        # tests if the typeerror is raised if length was not int or float (wrong type)
        with self.assertRaises(TypeError):
            square = Square('10')

    def test_length_with_zero_or_negative(self):
        # tests if the valueerror is raised if length is negative
        with self.assertRaises(ValueError):
            square = Square(0)
            square = Square(-1)


# you can also delete this main function
# and call python -m unittest -v (will find test modules)
if __name__ == "__main__":
    unittest.main(verbosity=2)