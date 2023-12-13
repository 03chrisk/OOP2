import os
import sys
sys.path.append(os.getcwd() + "/part_1/src/")
from CodeMaker import Codemaker
from codebreaker import Codebreaker


class Mastermind():
    def __init__(self, max_attempts):
        self.codemaker = Codemaker()
        self.codebreaker = Codebreaker()
        self.max_attempts = max_attempts
