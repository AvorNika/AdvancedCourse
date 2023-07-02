# раздел 16.3 экзамен Функции, задание 8
from operator import *


def arithmetic_operation(symbol):
    operations = {'+': add, '-': sub, '*': mul, '/': truediv}
    return operations[symbol]


print(arithmetic_operation('+')(20, 10))
print(arithmetic_operation('/')(20, 5))
