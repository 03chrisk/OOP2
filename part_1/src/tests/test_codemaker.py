import unittest
import sys
sys.path.append("..")
from codemaker import Codemaker


class Tests(unittest.TestCase):
    def setUp(self):
        self.codemaker = Codemaker()

    def test_symbols_attribute(self):
        self.assertIsNotNone(self.codemaker.symbols)

    def test_code_length_attribute(self):
        self.assertIsNotNone(self.codemaker.code_length)


if __name__ == "__main__":
    unittest.main()
