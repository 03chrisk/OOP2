import unittest
import os
import sys
sys.path.append("..")
from mastermind import Mastermind


class Tests(unittest.TestCase):

    def test_game_attributes(self):
        mastermind = Mastermind(attempts=10)
        self.assertEqual(mastermind.symbols, ["W", "B", "Y", "G", "R", "K"])
        self.assertEqual(mastermind.code_length, 4)
        self.assertEqual(mastermind._num_attempts, 10)


if __name__ == "__main__":
    unittest.main()
