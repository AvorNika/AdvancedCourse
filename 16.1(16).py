# раздел 16.1 экзамен Функции, задание 16 Pretty print

from functools import reduce


def pretty_print(data, side='-', delimiter='|'):
        for_print = reduce(lambda x, y: x + ' ' + str(y) + ' ' + delimiter, data, delimiter)
        user_side = ' ' + side * (len(for_print) - 2) + ' '
        print(user_side, for_print, user_side, sep='\n')


pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')
