# раздел 17.2 Работа с текстовыми файлами, задание 16 Общая стоимость
file = open('prices.txt', 'r', encoding='utf-8')

print(sum(map(lambda y: int(y[1]) * int(y[2]), map(lambda x: (x.rstrip()).split(), file.readlines()))))

file.close()
