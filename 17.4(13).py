# раздел 17.4 Работа с текстовыми файлами, задание 13* Конкатенация файлов
with open('output1.txt', 'w', encoding='utf-8') as output1:
    n = int(input())
    files = []
    for _ in range(n):
        files.append(input())
    for file in files:
        with open(file, 'r', encoding='utf-8') as new_file:
            for line in new_file:
                output1.write(line)
