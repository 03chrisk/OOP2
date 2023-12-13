import random


class Codemaker():
    def __init__(self):
        self.symbols = ["W", "B", "Y", "G", "R", "K"]
        self.code_length = 4
        self.secret_code = self.generate_code()

    def generate_code(self):
        return [random.choice(self.symbols) for _ in range(self.code_length)]
