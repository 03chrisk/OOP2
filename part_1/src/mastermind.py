import os
import sys
sys.path.append(os.getcwd() + "/part_1/src/")
from CodeMaker import Codemaker
from codebreaker import Codebreaker


class Mastermind():
    def __init__(self, max_attempts: int) -> None:
        self.__codemaker = Codemaker()
        self.__codebreaker = Codebreaker()
        self.__max_attempts = max_attempts

    @property
    def max_attempts(self):
        return self.__max_attempts

    @property
    def codemaker(self):
        return self.__codemaker

    @property
    def codebreaker(self):
        return self.__codebreaker

    def _evaluate_guess(self, guess: list) -> tuple[int, int]:

        """
        This method evaluates the user's guess by calculating the number of
        correct positions in the guess and the number of correct symbols.

        Args:
            A list with the user's guess

        Returns:
            A tuple of integers, correct_position and correct_symbol
        """

        correct_position = sum(
            a == b for a, b in zip(guess, self.codemaker.secret_code))

        secret_code_copy = list(self.codemaker.secret_code)

        for i, symbol in enumerate(guess):
            if symbol == self.codemaker.secret_code[i]:
                secret_code_copy[i] = None

        correct_symbol = 0
        for i, symbol in enumerate(guess):
            if symbol in secret_code_copy:
                if symbol != self.codemaker.secret_code[i]:
                    correct_symbol += 1
                    secret_code_copy.remove(symbol)

        return correct_position, correct_symbol

    def play(self) -> None:

        """
        This method calls the make_guess function and then evaluate_guess.
        If the user has guessed the correct code, the game ends. Otherwise,
        the loop continues until the user still has guesses left.

        Args:
            None

        Returns:
            None
        """

        for attempt in range(1, self.max_attempts + 1):
            guess = self.codebreaker.make_guess()
            correct_position, correct_symbol = self._evaluate_guess(guess)
            print(f"Attempt {attempt}: {correct_position} correct positions,\
                 {correct_symbol} correct guesses in the wrong position.")

            if correct_position == 4:
                print("Congratulations! You've cracked the code.")
                return

        print("Game Over. The correct code was:", ''.join(
            self.codemaker.secret_code))
