from random import randint, choice


def make_one_special_char():
    # 32-47 58-64 91-96 123-126
    ranges = [
        randint(32, 47),
        randint(58, 64),
        randint(91, 96),
        randint(123, 126),
    ]
    ascii_int = choice(ranges)
    return chr(ascii_int)


def make_one_uppercase_letter():
    ascii_int = randint(65, 90)
    return chr(ascii_int)


def make_one_lowercase_letter():
    ascii_int = randint(97, 122)
    return chr(ascii_int)


def make_one_number():
    number = randint(97, 122)
    return number
