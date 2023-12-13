import unittest
import os
import sys
sys.path.append(os.getcwd() + "/part_1/src/")
from mastermind import Mastermind


class Tests(unittest.TestCase):
    def setUp(self):
        self.mastermind = Mastermind(max_attempts=10)

    def test_max_attempts(self):
        self.assertIsNotNone(self.mastermind.max_attempts)


if __name__ == "__main__":
    unittest.main()
