# раздел 18.1 экзамен Работа с файлами, задание 3 Goooood students
with open('grades.txt', 'r', encoding='utf-8') as file:
    data = list(map(lambda x: x.rstrip().split(), file.readlines()))
    counter = 0
    for elem in data:
        if int(elem[1]) >= 65 and int(elem[2]) >= 65 and int(elem[3]) >= 65:
            counter += 1
    print(counter)
