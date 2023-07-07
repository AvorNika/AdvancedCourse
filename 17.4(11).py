# раздел 17.4 Работа с текстовыми файлами, задание 11 Подарок на новый год
with open('class_scores.txt', 'r', encoding='utf-8') as class_scores, open('new_scores.txt', 'w', encoding='utf-8') as new_scores:
    for line in class_scores:
        new_line = [line.rstrip().split()[0], (int(line.rstrip().split()[1]) + 5)]
        if new_line[1] > 100:
            new_line[1] = 100
        print(f'{new_line[0]} {new_line[1]}', file=new_scores)
