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


if __name__ == "__main__":
    unittest.main()
