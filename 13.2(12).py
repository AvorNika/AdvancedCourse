# раздел 13.2 Модуль fractions, задание 12* Юный математик
from fractions import Fraction
from math import gcd
n = int(input())
i, j = 0, n-1
numbers = [a for a in range(1, n+1)]
result = []

while j > i:
    while numbers[i] + numbers[j] != n:
        if numbers[i] + numbers[j] > n:
            j -= 1
        elif numbers[i] + numbers[j] < n:
            i += 1
    if numbers[i] + numbers[j] == n:
        if gcd(numbers[i], numbers[j]) == 1:
            result.append(Fraction(numbers[i], numbers[j]))
            i += 1
            j -= 1
        else:
            i += 1
            j -= 1

print(max(result))
