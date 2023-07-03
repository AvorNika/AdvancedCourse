# раздел 17.2 Работа с текстовыми файлами, задание 14 Сумма двух-1
file = open('numbers.txt', 'r', encoding='utf-8')

print(sum(map(lambda x: int(x.rstrip()), file.readlines())))

file.close()
