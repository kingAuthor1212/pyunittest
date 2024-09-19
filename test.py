import unittest
from cal import addNumbers, subNumbers
class MyTestCase(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(addNumbers(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(addNumbers(-1, -2), -3)

    def test_add_mixed_numbers(self):
        self.assertEqual(addNumbers(1, -2), -1)
        self.assertEqual(addNumbers(-1, 2), 1)
  def test_positive_numbers(self):
        self.assertEqual(subNumbers(5, 3), 2)

    def test_negative_numbers(self):
        self.assertEqual(subNumbers(-5, -3), -2)

    def test_zero(self):
        self.assertEqual(subNumbers(0, 0), 0)
        self.assertEqual(subNumbers(5, 0), 5)
        self.assertEqual(subNumbers(0, 5), -5)

    def test_mixed_numbers(self):
        self.assertEqual(subNumbers(10, 15), -5)
        self.assertEqual(subNumbers(-10, 15), -25)
        self.assertEqual(subNumbers(10, -15), 25)
if __name__ == '__main__':
    unittest.main()
