# раздел 9.2 экзамен, Множества, задание 9 Онлайн-школа BEEGEEK 3
m, n = int(input()), int(input())

list_math = {input() for _ in range(m)}
list_info = {input() for _ in range(n)}

if len(list_math ^ list_info) > 0:
    print(len(list_math ^ list_info))
else:
    print('NO')
