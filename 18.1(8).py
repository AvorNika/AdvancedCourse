# раздел 18.1 экзамен Работа с файлами, задание 8* Пропущенные комменты
with open('new.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    counter = 0
    for i in range(len(lines)):
        if lines[i].startswith('def'):
            if lines[i-1].startswith('#') is not True:
                counter += 1
                print(lines[i][4:lines[i].index('(')])
    if counter == 0:
        print('Best Programming Team')
