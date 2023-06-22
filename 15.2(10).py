# раздел 15.2 Функции с переменным количеством аргументов, задание 10
def count_args(*args):
    return len(args)


print(count_args())
print(count_args(10))
print(count_args('atepik', 'beegeek'))
print(count_args([], (''), 'a', 12, False))
