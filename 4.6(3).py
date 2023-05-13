# раздел 4.6 Матрицы, задание 3 Заполнение 1
user_string = input()
n = int(user_string.split()[0])
m = int(user_string.split()[1])

matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = m * i + j + 1

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end=' ')
    print()
