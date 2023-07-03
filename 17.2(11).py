# раздел 17.2 Работа с текстовыми файлами, задание 11 Содержимое файла
name = input()
file = open(name, 'r')
print(file.read())
file.close()
