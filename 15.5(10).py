# раздел 15.5 Функции высшего порядка, задание 10


def map(function, items):
    result = []
    for item in items:
        result.append(function(item, 2))
    return result


numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]

new_numbers = map(round, numbers)
print(*new_numbers, sep='\n')
