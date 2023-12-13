import os
import sys
sys.path.append(os.getcwd() + "/part_1/src/")


class Codemaker():
    def __init__(self):
        self.symbols = ["W", "B", "Y", "G", "R", "K"]
        self.code_length = None
        self.secret_code = None
