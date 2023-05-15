# раздел 5.1 Итоговая работа по вложенным спискам, экзамен, задание 8 Диагонали, параллельные главной
n = int(input())
matrix = [[0] * n for _ in range(n)]

for q in range(n):
    for i in range(n):
        for j in range(n):
            if abs(i - j) == q:
                matrix[i][j] = q

for r in range(n):
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()
