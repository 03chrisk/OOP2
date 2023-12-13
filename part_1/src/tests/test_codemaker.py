import unittest
import os
import sys
sys.path.append(os.getcwd() + "/part_1/src/")
from CodeMaker import Codemaker


class Tests(unittest.TestCase):
    def setUp(self):
        self.codemaker = Codemaker()

    def test_symbols_attribute(self):
        self.assertIsNotNone(self.codemaker.symbols)

    def test_code_length_attribute(self):
        self.assertIsNotNone(self.codemaker.code_length)
        self.assertEqual(self.codemaker.code_length, 4)

    def test_secret_code(self):
        self.assertIsNotNone(self.codemaker.secret_code)
        self.assertEqual(len(self.codemaker.secret_code),
                         self.codemaker.code_length)

    def test_secret_code_symbols(self):
        for symbol in self.codemaker.secret_code:
            self.assertIn(symbol, ["W", "B", "Y", "G", "R", "K"])


if __name__ == "__main__":
    unittest.main()
