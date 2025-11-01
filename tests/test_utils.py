import unittest
from src.utils import calculate, greet

class TestUtils(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(calculate(2, 3), 5)
        self.assertEqual(calculate(-1, 1), 0)

    def test_greet(self):
        self.assertEqual(greet("Alice"), "Bonjour, Alice!")


if __name__ == '__main__':
    unittest.main()
