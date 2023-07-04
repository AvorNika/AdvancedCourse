# раздел 17.3 Работа с текстовыми файлами, задание 8 Обратный порядок
with open('data.txt', 'r', encoding='utf-8') as file:
    lines = list(map(lambda x: x.rstrip(), file.readlines()))
    print(*lines[::-1], sep='\n')
