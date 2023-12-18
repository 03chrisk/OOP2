import random


class Codemaker():
    def __init__(self) -> None:
        self.__symbols = ["W", "B", "Y", "G", "R", "K"]
        self.__code_length = 4
        self.__secret_code = self.__generate_code()

    @property
    def symbols(self):
        return self.__symbols

    @property
    def code_length(self):
        return self.__code_length

    @property
    def secret_code(self):
        return self.__secret_code

    @secret_code.setter
    def secret_code(self, new_code):
        if isinstance(new_code, list) and len(new_code) == self.code_length:
            if all(symbol in self.__symbols for symbol in new_code):
                self.__secret_code = new_code
            else:
                raise ValueError("New code contains invalid symbols.")
        else:
            raise ValueError("New code must be a list of length {}"
                             .format(self.__code_length))

    def __generate_code(self) -> list:

        """
        Randomly generates a code by using only the colours specified in
        self.symbols.

        Args:
            None

        Returns:
            A list with the generated code (containing 4 letters)
        """

        return [random.choice(self.symbols) for _ in range(self.code_length)]
