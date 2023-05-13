# раздел 4.6 Матрицы, задание 1 Шахматная доска
user_string = input()
n = int(user_string.split()[0])
m = int(user_string.split()[1])
matrix = [['.' for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if (i + j) % 2 != 0:
            matrix[i][j] = '*'

for r in range(n):
    for c in range(m):
        print(matrix[r][c], end=' ')
    print()
