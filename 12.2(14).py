# раздел 12.2 модуль random, задание 14* Генератор паролей 2
import random
import string
n, m = int(input()), int(input())


def generate_password(length):
    upper_letters = set(string.ascii_uppercase) - set('IO')
    lower_letters = set(string.ascii_lowercase) - set('ol')
    digits = set(string.digits) - set('01')
    symbols = list(upper_letters) + list(lower_letters) + list(digits)

    password = random.sample(symbols, length)
    upper_char = random.choice(list(upper_letters))
    lower_char = random.choice(list(lower_letters))
    digit = random.choice(list(digits))
    indexes = random.sample(range(length), 3)
    password[indexes[0]] = upper_char
    password[indexes[1]] = lower_char
    password[indexes[2]] = digit
    return ''.join(password)


def generate_passwords(count, length):
    list_of_passwords = []
    for _ in range(count):
        list_of_passwords.append(generate_password(length))

    return list_of_passwords


print(*generate_passwords(n, m), sep='\n')
