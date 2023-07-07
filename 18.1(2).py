# раздел 18.1 экзамен Работа с файлами, задание 2 Суммарная стоимость
with open('ledger.txt', 'r', encoding='utf-8') as file:
    info = list(map(lambda x: int(x.rstrip()[1:]), file.readlines()))
    print(f'${sum(info)}')
