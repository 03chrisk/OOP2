import random


class Codemaker():
    def __init__(self) -> None:
        self.__symbols = ["W", "B", "Y", "G", "R", "K"]
        self.__code_length = 4
        self.__secret_code = self.generate_code()

    @property
    def symbols(self):
        return self.__symbols

    @property
    def code_length(self):
        return self.__code_length

    @property
    def secret_code(self):
        return self.__secret_code

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
