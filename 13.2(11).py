# раздел 13.2 Модуль fractions, задание 11 Сумма дробей 2
from fractions import Fraction
from math import factorial
n = int(input())
result = 0
for i in range(1, n+1):
    result += 1 / (Fraction(factorial(i)))

print(result)
