# раздел 5.1 Итоговая работа по вложенным спискам, экзамен, задание 4 Снежинка
n = int(input())
matrix = [['.'] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j or i == n - 1 - j or i == n // 2 or j == n // 2:
            matrix[i][j] = '*'

for r in range(n):
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()
