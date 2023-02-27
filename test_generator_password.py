"""
https://en.wikipedia.org/wiki/List_of_Unicode_characters
Funções
    criar caractere especial baseado na tabela unicode
        Ranges: 32-47 58-64 91-96 123-126 -> [ -\/:-@\[-`{-~]
    criar letras maiúsculas baseado na tabela unicode
        Ranges: 65-90
    criar letras minúsculas baseado na tabela unicode
        Ranges: 97-122
    criar números baseado na tabela unicode
        Ranges: 48-57
    criar senha com:
        possibilidade de escolha dos caracteres (letras, números, etc)
        possibilidade de escolha do tamanho da senha (min = 4)
"""

import unittest
import re
from generator_password import make_one_special_char, make_one_uppercase_letter, make_one_lowercase_letter, \
    make_one_number


class TestMakeOneSpecialChar(unittest.TestCase):
    def test_make_one_special_char_multiple_ranges(self):
        regex = re.compile(r'^[ -\/:-@\[-`{-~]$')

        for i in range(100):
            with self.subTest(i=i):
                result = make_one_special_char()
                self.assertRegex(result, regex)


class TestMakeOneUppercaseLetter(unittest.TestCase):
    def test_make_one_uppercase_letter_range_65_90(self):
        regex = re.compile(r'^[A-Z]$')

        for i in range(100):
            with self.subTest(i=i):
                result = make_one_uppercase_letter()
                self.assertRegex(result, regex)


class TestMakeOneLowercaseLetter(unittest.TestCase):
    def test_make_one_lowercase_letter_range_65_90(self):
        regex = re.compile(r'^[a-z]$')

        for i in range(100):
            with self.subTest(i=i):
                result = make_one_lowercase_letter()
                self.assertRegex(result, regex)


class TestMakeOneNumber(unittest.TestCase):
    def test_make_one_number_range_ascii_48_57(self):
        ord_range = list(range(48, 58))

        for i in range(100):
            with self.subTest(i=i):
                result = make_one_number()
                self.assertIn(result, ord_range)


if __name__ == '__main__':
    unittest.main(verbosity=2)
