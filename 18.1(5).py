# раздел 18.1 экзамен Работа с файлами, задание 5 Tail of a File
with open(input(), 'r', encoding='utf-8') as file:
    data = []
    for line in file:
        if len(data) < 10:
            data.append(line.rstrip())
        else:
            del data[0]
            data.append(line.rstrip())
    print(*data, sep='\n')

    # data = list(map(lambda x: x.rstrip(), file.readlines()))
    # print(*data[-10:], sep='\n')
