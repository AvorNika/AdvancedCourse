# раздел 17.3 Работа с текстовыми файлами, задание 7 Переворот строки
with open('text.txt', 'r', encoding='utf-8') as file:
    print(file.readline().rstrip()[::-1])
