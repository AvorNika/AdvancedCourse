# раздел 17.4 Работа с текстовыми файлами, задание 12* Загадка от Жака Фреско
with open('goats.txt', 'r', encoding='utf-8') as goats, open('answer.txt', 'w', encoding='utf-8') as answer:
    data = list(map(lambda x: x.rstrip(), goats.readlines()))
    del data[0]
    colours = {}
    for d in data:
        if d != 'GOATS':
            colours[d] = 0
        else:
             break
    del data[:len(colours) + 1]
    for elem in data:
        colours[elem] += 1
    result = []
    for key, value in colours.items():
        if value * 100 / sum(colours.values()) > 7:
            result.append(key)
    result.sort()
    for res in result:
        print(res, file=answer)

