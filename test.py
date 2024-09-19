import unittest
from cal import addNumbers
class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(addNumbers(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(addNumbers(-1, -2), -3)

    def test_add_mixed_numbers(self):
        self.assertEqual(addNumbers(1, -2), -1)
        self.assertEqual(addNumbers(-1, 2), 1)

if __name__ == '__main__':
    unittest.main()
