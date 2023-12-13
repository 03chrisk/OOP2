import os
import sys
sys.path.append(os.getcwd() + "/part_1/src/")


class Codebreaker():
    def make_guess(self):
        while True:
            guess = input().upper()
            if all(char in ["W", "B", "Y", "G", "R", "K"]
                    for char in guess) and len(guess) == 4:
                return guess
