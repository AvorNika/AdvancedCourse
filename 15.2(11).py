# раздел 15.2 Функции с переменным количеством аргументов, задание 11
def sq_sum(*args):
    sum1 = 0
    for elem in args:
        sum1 += elem**2
    return sum1


print(sq_sum())
print(sq_sum(2))
print(sq_sum(1.5, 2.5))
print(sq_sum(1, 2, 3))
print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
