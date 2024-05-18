# this file will mock the read function

import unittest
from unittest.mock import MagicMock
import total

class TestTotal(unittest.TestCase):
    def test_calculate_total(self):
        total.read = MagicMock() # mock the read function from total module
        total.read.return_value = [1, 2, 3] # assign the return of value of mock
        result = total.calculate_total('') # empty filename as input
        self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main(verbosity=2)