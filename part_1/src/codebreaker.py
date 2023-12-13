import os
import sys
sys.path.append(os.getcwd() + "/part_1/src/")


class Codebreaker():
    def make_guess(self):
        while True:
            guess = input().upper()
            if len(guess) == 4:
                return guess
