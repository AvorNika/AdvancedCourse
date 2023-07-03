# раздел 17.2 Работа с текстовыми файлами, задание 13 Случайная строка
from random import randrange
file = open('lines.txt', 'r', encoding='utf-8')
content = file.readlines()
num = randrange(len(content))
print(content[num].rstrip())
file.close()
