# раздел 12.2 модуль random, задание 6
import random


def generate_ip():

    numbers = []
    for _ in range(4):
        num = random.randrange(256)
        numbers.append(str(num))
    return '.'.join(numbers)


print(generate_ip())
