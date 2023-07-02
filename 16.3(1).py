# раздел 16.3 экзамен Функции, задание 1


def concat(*args, sep=' '):
    result = []
    for arg in args:
        if isinstance(arg, int):
            arg = str(arg)
            result.append(arg)
        else:
            result = list(args)

    return sep.join(result)


print(concat('hello', 'python', 'and', 'stepik'))
print(concat('hello', 'python', 'and', 'stepik', sep='*'))
print(concat('hello', 'python', sep='()()()'))
print(concat('hello', sep='()'))
print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))
