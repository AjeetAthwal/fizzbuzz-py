import unittest
from main import fizz, buzz, num_to_str_modulo

class TestNumToStringModuloMethod(unittest.TestCase):

    def test_num_to_string_modulo(self):
        num = 0
        mod = 2
        string = "rand"
        self.assertEqual("rand", num_to_str_modulo(num, mod, string))

    def test_non_zero_num_to_string_modulo(self):
        mod = 2
        num = mod
        string = "rand"
        self.assertEqual("rand", num_to_str_modulo(num, mod, string))        

    def test_num_to_string_modulo(self):
        num = 1
        mod = 2
        string = "rand"
        self.assertEqual("", num_to_str_modulo(num, mod, string))

class TestFizzMethod(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual("fizz", fizz(0))

    def test_non_fizz(self):
        num = 1
        self.assertEqual("", fizz(num))

class TestBuzzMethod(unittest.TestCase):

    def test_buzz(self):
        self.assertEqual("buzz", buzz(0))

    def test_non_buzz(self):
        num = 1
        self.assertEqual("", buzz(num))

if __name__ == '__main__':
    unittest.main()