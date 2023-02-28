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
    number = randint(48, 57)
    return chr(number)


def make_password(length: int = 16, chars: bool = True, upper: bool = True, lower: bool = True, numbers: bool = True) -> str:
    assert isinstance(length, int), 'length is not int'
    assert length >= 16, 'length should be great than 4'
    assert length <= 1000, 'length should be great than 4'

    new_password = []
    while len(new_password) < length:
        chars and new_password.append(str(make_one_special_char()))
        if len(new_password) >= length:
            break

        upper and new_password.append(str(make_one_uppercase_letter()))
        if len(new_password) >= length:
            break

        lower and new_password.append(str(make_one_lowercase_letter()))
        if len(new_password) >= length:
            break

        numbers and new_password.append(str(make_one_number()))
        if len(new_password) >= length:
            break

    new_password_formatted = ''.join(new_password)
    return new_password_formatted
