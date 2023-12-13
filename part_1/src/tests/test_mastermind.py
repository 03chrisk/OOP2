import unittest
import os
import sys
sys.path.append("..")
from mastermind import Mastermind


class Tests(unittest.TestCase):

    def test_get_symbols(self):
        mastermind = Mastermind()
        self.assertEqual(mastermind.symbols, ["W", "B", "Y", "G", "R", "K"])


if __name__ == "__main__":
    unittest.main()
