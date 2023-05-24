# раздел 8.7 Методы множеств, задание 8 Одинаковые цифры
num1, num2 = input(), input()
if set(num1).isdisjoint(set(num2)):
    print('NO')
else:
    print('YES')
