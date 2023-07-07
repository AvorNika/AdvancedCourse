# раздел 17.4 Работа с текстовыми файлами, задание 9 Случайные числа
from random import randint
with open('random.txt', 'w', encoding='utf-8') as random:
    for _ in range(25):
        print(randint(111, 777), file=random)
