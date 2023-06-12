# раздел 12.2 модуль random, задание 7
import random
import string


def generate_index():
    ind = ''

    for _ in range(2):
        sym1 = random.choice(string.ascii_uppercase)
        ind += sym1

    numbers = []
    for _ in range(2):
        dig = random.randrange(100)
        numbers.append(str(dig))
    ind += '_'.join(numbers)

    for _ in range(2):
        sym2 = random.choice(string.ascii_uppercase)
        ind += sym2

    return ind


print(generate_index())
