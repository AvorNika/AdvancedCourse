# раздел 15.9 Встроенные функции any(), all(), zip(), enumerate(), задание 12 Интересные числа
a, b = int(input()), int(input())


def check(num):
    if all(map(lambda c: int(c) > 0 and num % int(c) == 0, str(num))):
        return num


result = list(filter(check, range(a, b+1)))

print(*result)

