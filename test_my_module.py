import unittest


def setUpModule():
    print('Running setUpModule')


def tearDownModule():
    print('\nRunning tearDownModule')


class TestMyModule(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(5+5, 10)

    def test_case_2(self):
        self.assertEqual(1+1, 2)

if __name__ == "__main__":
    unittest.main()