# раздел 12.1 Модуль random, задание 11
import random

n = int(input())    # количество попыток
for _ in range(n):
    result = random.randint(0, 1)
    if result == 0:
        print('Орел')
    else:
        print('Решка')
