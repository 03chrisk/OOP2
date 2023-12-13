import os
import sys
sys.path.append(os.getcwd() + "/part_1/src/")


class Codebreaker():
    def make_guess(self):
        while True:
            guess = input()
            return guess
