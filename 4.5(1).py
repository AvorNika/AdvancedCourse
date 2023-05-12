# раздел 4.5 Матрицы, задание 1 Таблица умножения
n, m = int(input()), int(input())

mult = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        mult[i][j] = i * j
        print(str(mult[i][j]).ljust(3), end=' ')
    print()
