import unittest
from unittest.mock import patch
import total

class TestTotal(unittest.TestCase):

    @patch('total.read') # the target is the read function of the total module
    def test_calculate_total(self, mock_read):
        # the total.read will be replace the mock_read
        mock_read.return_value = [1, 2, 3]
        result = total.calculate_total('')
        self.assertEqual(result, 6)

    def test_calculate_total_2(self):
        with patch('total.read') as mock_read:
            mock_read.return_value = [1, 2, 3]
            result = total.calculate_total('')
            self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main(verbosity=2)