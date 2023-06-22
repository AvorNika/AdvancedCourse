# раздел 15.2 Функции с переменным количеством аргументов, задание 14


def print_products(*args):
    counter = 0
    for arg in args:
        if isinstance(arg, str) and len(arg) > 0:
            counter += 1
            print(f'{counter}) {arg}')
        else:
            continue
    if counter == 0:
        print('Нет продуктов')


print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print_products([4], {}, 1, 2, {'Beegeek'}, '')
