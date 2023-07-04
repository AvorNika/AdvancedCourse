# раздел 17.3 Работа с текстовыми файлами, задание 9 Длинные строки
with open('lines.txt', 'r', encoding='utf-8') as file:
    lines = list(map(lambda x: x.rstrip(), file.readlines()))
    max_len = len(max(lines, key=len))
print(*list(filter(lambda y: len(y) == max_len, lines)), sep='\n')
