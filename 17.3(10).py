# раздел 17.3 Работа с текстовыми файлами, задание 10 Сумма чисел в строках
with open('numbers.txt', 'r', encoding='utf-8') as file:
    lines = list(map(lambda x: x.strip().split(), file.readlines()))
    sum_lines = []
    for line in lines:
        new_line = list(map(lambda y: int(y), line))
        sum_lines.append(sum(new_line))
print(*sum_lines, sep='\n')
