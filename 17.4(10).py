# раздел 17.4 Работа с текстовыми файлами, задание 10 Нумерация строк
with open('input.txt', 'r', encoding='utf-8') as file, open('output.txt', 'w', encoding='utf-8') as output:
    for num, line in enumerate(file, 1):
        print(f'{num}) {line.rstrip()}', file=output)
