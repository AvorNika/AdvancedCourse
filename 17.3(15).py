# раздел 17.3 Работа с текстовыми файлами, задание 15 CSV-файл
def read_csv():
    with open('data.csv', 'r', encoding='utf-8') as file:
        result = []

        first_line = file.readline().rstrip().split(',')
        for line in file:
            result.append(dict(zip(first_line, line.rstrip().split(','))))
    return result


print(*read_csv(), sep='\n')
