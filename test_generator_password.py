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
from generator_password import make_one_special_char


class TestPasswordGenerator(unittest.TestCase):
    def test_make_one_special_char_multiple_ranges(self):
        regex = re.compile(r'^[ -\/:-@\[-`{-~]$')

        for i in range(10000):
            with self.subTest(i=i):
                result = make_one_special_char()
                self.assertRegex(result, regex)


if __name__ == '__main__':
    unittest.main(verbosity=2)
