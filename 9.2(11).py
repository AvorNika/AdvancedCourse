# раздел 9.2 экзамен, Множества, задание 11* Онлайн-школа BEEGEEK 5
m, n = int(input()), int(input())

list_of_all = [input() for _ in range(m+n)]

list_of_students = set(list_of_all)

result = m + n - 2 * ((m + n) - len(list_of_students))

if result > 0:
    print(result)
else:
    print('NO')
