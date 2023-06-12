# раздел 12.1 модуль random, задание 12
import random

n = int(input())    # количество попыток
for _ in range(n):
    print(random.randint(1, 6))
