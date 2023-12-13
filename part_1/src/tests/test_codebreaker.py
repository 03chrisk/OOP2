import unittest
import os
import sys
sys.path.append(os.getcwd() + "/part_1/src/")
from codebreaker import Codebreaker


class Tests(unittest.TestCase):
    def setUp(self):
        self.codebreaker = Codebreaker()

    def test_guess_existence(self):
        self.assertIsNotNone(self.codebreaker.make_guess())


if __name__ == "__main__":
    unittest.main()
