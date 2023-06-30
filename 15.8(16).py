# раздел 15.8 Анонимные функции, задание 16* Значение многочлена
from functools import reduce
coef = [int(c) for c in input().split()][::-1]
n = int(input())


def evaluate(coefficients, x):
    indexes = [i[0] for i in enumerate(coefficients)]
    result = reduce(lambda a0, a1: a0 + a1, map(lambda co, ind: co * x ** ind, coefficients, indexes))
    print(result)


evaluate(coef, n)
