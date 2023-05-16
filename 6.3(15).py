# раздел 6.3 Основы работы с кортежами, задание 15 Последовательность Трибоначчи
n = int(input())
tr1, tr2, tr3 = 1, 1, 1
result = []

for i in range(n):
    result.append(tr1)
    tr1, tr2, tr3 = tr2, tr3, tr1 + tr2 + tr3

print(*result)
