import unittest
from square import Square

class TestSquare(unittest.TestCase):
    def test_area(self):
        square = Square(10)
        area = square.area()
        self.assertEqual(area, 100)


# you can also delete this main function
# and call python -m unittest -v (will find test modules)
if __name__ == "__main__":
    unittest.main(verbosity=2)