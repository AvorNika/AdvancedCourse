# раздел 17.3 Работа с текстовыми файлами, задание 14 Необычные страны
with open('population.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    # for line in lines:
    #     new_line = line.rstrip().split()
    #     if int(new_line[-1]) > 500000 and new_line[0][0] == 'G':
    #         print(new_line[0])
    result = map(lambda y: y[0], filter(lambda x: x[0][0] == 'G' and int(x[-1]) > 500000, map(lambda x: x[:-1].split('\t'), lines)))
print(*result, sep='\n')
