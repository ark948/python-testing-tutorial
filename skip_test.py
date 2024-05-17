import unittest
from sys import platform


class TestDemo(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1+1, 2)

    # this can also be used on an entire test class
    @unittest.skip('Work in progress')
    def test_case_2(self):
        pass

    def test_case_3(self):
        self.skipTest('Work in progress')

    def test_case_4(self):
        raise unittest.SkipTest('Work in progress')
    
    @unittest.skipIf(platform.startswith("win"), "Do not run on Windows.")
    def test_only_for_linux(self):
        self.assertIsNotNone([])

if __name__ == "__main__":
    unittest.main(verbosity=2)