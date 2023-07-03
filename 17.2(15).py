# раздел 17.2 Работа с текстовыми файлами, задание 15 Сумма двух-2
file = open('nums.txt', 'r', encoding='utf-8')

print(sum(map(lambda x: int(x), map(lambda y: y.replace('\n', ''), file.read().split()))))

file.close()
