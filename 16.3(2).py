# раздел 16.3 экзамен Функции, задание 2
from functools import reduce


def product_of_odds(data):
    result = reduce(lambda x, y: x * y, filter(lambda c: c % 2 == 1, data), 1)
    return result


print(product_of_odds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
