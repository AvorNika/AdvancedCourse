# раздел 4.6 Матрицы, задание 8 Заполнение змейкой
user_string = input()
n = int(user_string.split()[0])
m = int(user_string.split()[1])
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            matrix[i][j] = i * m + j + 1
        elif i % 2 == 1:
            matrix[i][j] = m * (i + 1) - j

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end=' ')
    print()
