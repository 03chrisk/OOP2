import os
import sys
sys.path.append(os.getcwd() + "/part_1/src/")
from CodeMaker import Codemaker
from codebreaker import Codebreaker


class Mastermind():
    def __init__(self, max_attempts:int) -> None:
        self.codemaker = Codemaker()
        self.codebreaker = Codebreaker()
        self.max_attempts = max_attempts

    def evaluate_guess(self, guess:list) -> tuple[int, int]:
        correct_position = sum(
            a == b for a, b in zip(guess, self.codemaker.secret_code))

        secret_code_copy = list(self.codemaker.secret_code)
        correct_symbol = 0
        for i, symbol in enumerate(guess):
            if symbol in secret_code_copy:
                if symbol != self.codemaker.secret_code[i]:
                    correct_symbol += 1
        return correct_position, correct_symbol

    def play(self) -> None:
        for attempt in range(1, self.max_attempts + 1):
            guess = self.codebreaker.make_guess()
            correct_position, correct_symbol = self.evaluate_guess(guess)
            print(f"Attempt {attempt}: {correct_position} correct positions,\
                 {correct_symbol} correct guesses in the wrong position.")

            if correct_position == 4:
                print("Congratulations! You've cracked the code.")
                return

        print("Game Over. The correct code was:", ''.join(
            self.codemaker.secret_code))
