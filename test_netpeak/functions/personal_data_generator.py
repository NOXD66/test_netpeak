import random
import string


def random_string(string_length=None):
    if not string_length:
        string_length = random.randint(2, 12)
    else:
        string_length = string_length
        assert isinstance(string_length, int), 'Ошибка ввода данных'

    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


def random_email():
    return random_string() + '@' + random_string(6) + '.' + random_string(2)


def random_phone_number():
    return '+380' + ''.join(str(random.randint(0, 9)) for i in range(9))