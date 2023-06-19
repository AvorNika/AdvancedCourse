# раздел 13.2 Модуль fractions, задание 9 Операции над дробями
from fractions import Fraction
num1, num2 = input(), input()
print(f'{num1} + {num2} = {Fraction(num1) + Fraction(num2)}')
print(f'{num1} - {num2} = {Fraction(num1) - Fraction(num2)}')
print(f'{num1} * {num2} = {Fraction(num1) * Fraction(num2)}')
print(f'{num1} / {num2} = {Fraction(num1) / Fraction(num2)}')
