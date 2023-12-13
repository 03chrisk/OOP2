
class Mastermind:

    def __init__(self, attempts):
        self._symbols = ["W", "B", "Y", "G", "R", "K"]
        self._code_length = 4
        self._num_attempts = attempts

    @property
    def symbols(self):
        return self._symbols

    @property
    def code_length(self):
        return self._code_length

    @property
    def num_attempts(self):
        return self._num_attempts
