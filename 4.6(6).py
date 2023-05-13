# раздел 4.6 Матрицы, задание 6 Заполнение 4
n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j or i == n - j - 1 or i < j and i < n - 1 - j or i > j and i > n - 1 - j:
            matrix[i][j] = 1

for r in range(n):
    for c in range(n):
        print(str(matrix[r][c]).ljust(3), end=' ')
    print()
