import unittest
import os
import sys
sys.path.append(os.getcwd() + "/part_1/src/")
from mastermind import Mastermind


class Tests(unittest.TestCase):
    def setUp(self):
        self.mastermind = Mastermind(max_attempts=10)
        # Mocking the secret code
        self.mastermind.codemaker.secret_code = ['W', 'B', 'Y', 'G']

    def test_max_attempts(self):
        self.assertIsNotNone(self.mastermind.max_attempts)

    def test_if_eval_returns_something(self):
        guess = ['W', 'B', 'Y', 'G']
        self.assertIsNotNone(self.mastermind.evaluate_guess(guess))


if __name__ == "__main__":
    unittest.main()
