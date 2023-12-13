import unittest
from unittest.mock import patch
import os
import sys
sys.path.append(os.getcwd() + "/part_1/src/")
from codebreaker import Codebreaker


class Tests(unittest.TestCase):
    def setUp(self):
        self.codebreaker = Codebreaker()

    @patch('builtins.input', return_value='abc')
    def test_guess_existence(self, mock_input):
        guess = self.codebreaker.make_guess()
        self.assertEqual(guess, 'abc')

    @patch('builtins.input', side_effect=["ABC", "WXYZ"])
    def test_guess_length(self, mock_input):
        guess = self.codebreaker.make_guess()
        self.assertEqual(len(guess), 4)


if __name__ == "__main__":
    unittest.main()
