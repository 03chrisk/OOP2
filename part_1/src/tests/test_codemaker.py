import unittest
import os
import sys
sys.path.append(os.getcwd() + "/part_1/src/")
from codemaker import Codemaker


class Tests(unittest.TestCase):
    def setUp(self):
        self.codemaker = Codemaker()

    def test_symbols_attribute(self):
        self.assertIsNotNone(self.codemaker.symbols)


if __name__ == "__main__":
    unittest.main()
