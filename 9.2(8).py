# раздел 9.2 экзамен, Множества, задание 8 Онлайн-школа BEEGEEK 2
m, n = int(input()), int(input())

list_math = {input() for _ in range(m)}
list_info = {input() for _ in range(n)}

print(len(list_math - (list_math & list_info)))
