# раздел 8.7 Методы множеств, задание 9 Все цифры
num1, num2 = input(), input()
if set(num2).issubset(set(num1)):
    print('YES')
else:
    print('NO')
