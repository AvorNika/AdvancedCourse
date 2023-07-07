# раздел 18.1 экзамен Работа с файлами, задание 1 Количество строк в файле
with open(input(), 'r', encoding='utf-8') as file:
    print(len(file.readlines()))
