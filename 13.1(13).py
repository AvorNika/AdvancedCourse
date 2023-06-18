# раздел 13.1 Модуль decimal, задание 13 Математическое выражение
from decimal import *
d = Decimal(input())

result = d.exp() + d.ln() + d.log10() + d.sqrt()
print(result)
