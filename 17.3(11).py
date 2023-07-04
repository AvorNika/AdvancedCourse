# раздел 17.3 Работа с текстовыми файлами, задание 11 Сумма чисел в файле
with open('nums.txt', 'r', encoding='utf-8') as file:
    lines = list(map(lambda x: x.strip(), file.readlines()))
    new_lines = []
    for line in lines:
        new_line = ''
        for elem in line:
            if elem.isdigit():
                new_line += elem
            else:
                new_line += ' '
        result_line = list(map(lambda z: int(z), new_line.split()))
        new_lines.append(sum(result_line))
print(sum(new_lines))
