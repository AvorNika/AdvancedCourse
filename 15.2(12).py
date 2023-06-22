# раздел 15.2 Функции с переменным количеством аргументов, задание 12
def mean(*args):
    sum_args = 0
    count_args = 0
    for arg in args:
        if arg is not True and arg is not False and (isinstance(arg, int) or isinstance(arg, float)):
            sum_args += arg
            count_args += 1
    if count_args > 0:
        return sum_args / count_args
    else:
        return 0.0


print(mean())
print(mean(7))
print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
print(mean(True, ['stepik'], 'beegeek', (1, 2)))
print(mean(-1, 2, 3, 10, ('5')))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
