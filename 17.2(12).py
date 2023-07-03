# раздел 17.2 Работа с текстовыми файлами, задание 12 Предпоследняя строка
name = input()
file = open(name, 'r')

print(list(file)[-2].rstrip())

file.close()
