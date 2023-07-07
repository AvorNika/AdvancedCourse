# раздел 18.1 экзамен Работа с файлами, задание 4 Самое длинное слово в файле
with open('words.txt', 'r', encoding='utf-8') as file:
    data = file.readline().split()
    len_max = len(max(data, key=len))
    for elem in data:
        if len(elem) == len_max:
            print(elem)
