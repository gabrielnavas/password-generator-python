import unittest
import re
from generator_password import make_one_special_char, \
    make_one_uppercase_letter, \
    make_one_lowercase_letter, \
    make_one_number, \
    make_password


class TestMakeOneSpecialChar(unittest.TestCase):
    def test_make_one_special_char_multiple_ranges(self):
        regex = re.compile(r'^[ -/:-@\[-`{-~]$')

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


class TestPasswordLength(unittest.TestCase):
    values_min_max = [15, 1001]

    def test_make_password_length(self):
        for length in self.values_min_max:
            with self.assertRaises(AssertionError):
                make_password(length=length)

    def test_make_password_string(self):
        with self.assertRaises(AssertionError):
            make_password(length='a')


if __name__ == '__main__':
    unittest.main(verbosity=2)
