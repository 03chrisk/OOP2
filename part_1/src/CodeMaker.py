import random


class Codemaker():
    def __init__(self) -> None:
        self.symbols = ["W", "B", "Y", "G", "R", "K"]
        self.code_length = 4
        self.secret_code = self.generate_code()

    def generate_code(self) -> list:

        """
        Randomly generates a code by using only the colours specified in
        self.symbols.

        Args:
            None

        Returns:
            A list with the generated code (containing 4 letters)
        """

        return [random.choice(self.symbols) for _ in range(self.code_length)]
