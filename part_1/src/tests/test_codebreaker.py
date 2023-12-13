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


if __name__ == "__main__":
    unittest.main()
