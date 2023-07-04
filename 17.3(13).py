# раздел 17.3 Работа с текстовыми файлами, задание 13 Random name and surname
from random import randrange
with open('first_names.txt', 'r', encoding='utf-8') as file1, open('last_names.txt', 'r', encoding='utf-8') as file2:
    names = list(map(lambda x: x.rstrip(), file1.readlines()))
    surnames = list(map(lambda y: y.rstrip(), file2.readlines()))
    for _ in range(3):
        name = names[randrange(len(names))]
        surname = surnames[randrange(len(surnames))]
        print(name, surname)
