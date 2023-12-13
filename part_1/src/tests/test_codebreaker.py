import unittest
from unittest.mock import patch
import os
import sys
sys.path.append(os.getcwd() + "/part_1/src/")
from codebreaker import Codebreaker


class Tests(unittest.TestCase):
    def setUp(self):
        self.codebreaker = Codebreaker()

    @patch('builtins.input', side_effect=['abc', 'abcd'])
    def test_guess_not_none(self, mock_input):
        guess = self.codebreaker.make_guess()
        self.assertIsNotNone(guess)

    @patch('builtins.input', side_effect=['abc', 'abcd'])
    def test_guess_length(self, mock_input):
        guess = self.codebreaker.make_guess()
        self.assertEqual(len(guess), 4)

    @patch('builtins.input', return_value='abcd')
    def test_guess_uppercase(self, mock_input):
        guess = self.codebreaker.make_guess()
        self.assertTrue(all(char.isupper() for char in guess))

    @patch('builtins.input', side_effect=['WXYZ', 'WYBR'])
    def test_guess_valid_symbols(self, mock_input):
        guess = self.codebreaker.make_guess()
        self.assertTrue(all(
            char in ["W", "B", "Y", "G", "R", "K"] for char in guess))


if __name__ == "__main__":
    unittest.main()
