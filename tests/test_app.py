import unittest
from src.app import run_application

class TestApp(unittest.TestCase):
    def test_application_runs(self):
        result = run_application()
        self.assertIsNone(result)  # Supposer que la fonction ne retourne rien


if __name__ == '__main__':
    unittest.main()
