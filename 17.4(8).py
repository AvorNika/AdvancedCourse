# раздел 17.4 Работа с текстовыми файлами, задание 8 Входная строка
with open('output.txt', 'w', encoding='utf-8') as output:
    print(input(), file=output)
