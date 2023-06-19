# раздел 13.2 Модуль fractions, задание 13 Упорядоченные дроби
from fractions import Fraction
from math import gcd
n = int(input())
numbers = [a for a in range(1, n+1)]
result = []
for i in range(n):
    for j in range(n):
        if 0 < Fraction(numbers[i] / numbers[j]) < 1 and gcd(numbers[i], numbers[j]) == 1:
            result.append(Fraction(numbers[i], numbers[j]))

print(*sorted(result), sep='\n')
