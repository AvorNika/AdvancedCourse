# раздел 12.2 модуль random, задание 13 Генератор паролей 1
import random
import string
n, m = int(input()), int(input())


def generate_password(length):
    syms = string.ascii_letters + string.digits
    symbols = []
    for sym in syms:
        if sym not in 'oOlI10':
            symbols.append(sym)
    password = random.sample(symbols, length)
    return ''.join(password)


def generate_passwords(count, length):
    list_of_passwords = []
    for _ in range(count):
        list_of_passwords.append(generate_password(length))

    return list_of_passwords


print(*generate_passwords(n, m), sep='\n')
