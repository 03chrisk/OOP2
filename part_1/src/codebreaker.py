import os
import sys
sys.path.append(os.getcwd() + "/part_1/src/")


class Codebreaker():
    def make_guess(self) -> list:

        """
        This method prompts the user for input until they enter a valid guess.

        Args:
            None

        Returns:
            A list with the user's guess (containing 4 letters)
        """

        while True:
            guess = input("Enter your guess from the following letters : \
                W, B, Y, G, R, K. (e.g., WYBR): ").upper()
            if all(char in ["W", "B",
                            "Y", "G",
                            "R", "K"] for char in guess) and len(guess) == 4:
                return list(guess)
            print("Invalid input. Please use only W, B, Y, G, R, K and ensure\
                 the guess is 4 symbols long.")
