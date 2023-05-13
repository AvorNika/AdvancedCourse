# раздел 4.6 Матрицы, задание 2 Побочная диагональ
n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == n - j - 1:
            matrix[i][j] = 1
        elif i < n - 1 - j:
            matrix[i][j] = 0
        elif i > n - 1 - j:
            matrix[i][j] = 2

for r in range(n):
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()
