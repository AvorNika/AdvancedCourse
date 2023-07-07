# раздел 17.4 Работа с текстовыми файлами, задание 14* Лог файл
with open('logfile.txt', 'r', encoding='utf-8') as file, open('output2.txt', 'w', encoding='utf-8') as output2:
    data = list(map(lambda x: x.rstrip().split(', '), file.readlines()))
    for elem in data:
        if abs((int(elem[1].split(':')[0]) * 60 + int(elem[1].split(':')[1])) - (int(elem[2].split(':')[0]) * 60 + int(elem[2].split(':')[1]))) >= 60:
            print(elem[0], file=output2)
