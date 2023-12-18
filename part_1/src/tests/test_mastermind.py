import unittest
from unittest.mock import patch
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
        self.assertIsNotNone(self.mastermind._evaluate_guess(guess))

    def test_eval_guess_correct_position_and_symbol(self):
        # All correct
        guess = ['W', 'B', 'Y', 'G']
        correct_pos, correct_symbol = self.mastermind._evaluate_guess(guess)
        self.assertEqual(correct_pos, 4)
        self.assertEqual(correct_symbol, 0)

    def test_eval_guess_partial_correct(self):
        # All correct symbols but in wrong positions
        guess = ['B', 'W', 'G', 'Y']
        correct_pos, correct_symbol = self.mastermind._evaluate_guess(guess)
        self.assertEqual(correct_pos, 0)
        self.assertEqual(correct_symbol, 4)

    def test_eval_guess_mixed(self):
        # One correct position (W), one correct symbol but wrong position (G)
        guess = ['W', 'R', 'G', 'R']
        correct_pos, correct_symbol = self.mastermind._evaluate_guess(guess)
        self.assertEqual(correct_pos, 1)
        self.assertEqual(correct_symbol, 1)

    def test_eval_guess_none_correct(self):
        # None correct
        guess = ['R', 'R', 'R', 'R']
        correct_pos, correct_symbol = self.mastermind._evaluate_guess(guess)
        self.assertEqual(correct_pos, 0)
        self.assertEqual(correct_symbol, 0)

    @patch('builtins.input', side_effect=['BBBB', 'WBYG'])
    @patch('builtins.print')  # Mock print to suppress output during test
    def test_play_win(self, mock_print, mock_input):
        self.mastermind.play()
        mock_print.assert_any_call("Congratulations! You've cracked the code.")

    @patch('builtins.input', side_effect=['BBBB', 'YYYY', 'RRRR',
                                          'GGGG', 'WWWW', 'BBBB',
                                          'YYYY', 'RRRR', 'GGGG', 'WWWW'])
    @patch('builtins.print')  # Mock print
    def test_play_lose(self, mock_print, mock_input):
        self.mastermind.play()
        mock_print.assert_any_call(
            "Game Over. The correct code was:", ''.join(
                self.mastermind.codemaker.secret_code))


if __name__ == "__main__":
    unittest.main()
