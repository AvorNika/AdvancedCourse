# раздел 17.3 Работа с текстовыми файлами, задание 12 Статистика по файлу
from collections import Counter
with open('file.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    counter_letters = 0
    counter_words = 0
    counter_lines = len(lines)
    for line in lines:
        counter_words += len(line.split())
        for elem in line:
            if elem.isalpha():
                counter_letters += 1

print(f'Input file contains:\n{counter_letters} letters\n{counter_words} words\n{counter_lines} lines')
