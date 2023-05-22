# раздел 8.5 Методы множеств, задание 14 Встречалось ли число раньше?
n = input().split()
result = set()

for num in n:
    if int(num) in result:
        print('YES')
    else:
        print('NO')
        result.add(int(num))
