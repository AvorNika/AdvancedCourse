# раздел 13.2 Модуль fractions, задание 10 Сумма дробей 1
from fractions import Fraction
n = int(input())
result = 0
for i in range(1, n+1):
    result += 1 / (Fraction(i) ** 2)

print(result)
