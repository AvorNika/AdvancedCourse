# раздел 18.1 экзамен Работа с файлами, задание 6* Forbidden words
with open('forbidden_words.txt', 'r', encoding='utf-8') as forbidden_words, open(input(), 'r', encoding='utf-8') as file:
    f_w = list(map(lambda x: x.rstrip(), forbidden_words.readline().split()))

    data1 = ''
    for line in file:
        data1 += line
    data2 = data1.lower()[:]

    for word in f_w:
        if word in data2:
            data2 = data2.replace(word, '*'*len(word))

    i = 0
    counter = len(data1)
    result = ''
    while counter > 0:
        if data2[i] == '*':
            result += data2[i]
        else:
            result += data1[i]
        i += 1
        counter -= 1
    print(result)
