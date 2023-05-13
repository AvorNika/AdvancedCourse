# раздел 4.6 Матрицы, задание 10** Заполнение спиралью
user_string = input()
n = int(user_string.split()[0])
m = int(user_string.split()[1])
matrix = [[0] * m for _ in range(n)]
nm = 0

for q in range(n*m):
    i_min = q
    i_max = n - 1 - q
    j_min = q
    j_max = m - 1 - q
    for i in range(n):
        for j in range(m):
            if i == i_min and matrix[i][j] == 0:
                nm += 1
                matrix[i][j] = nm
            elif j == j_max and i != i_min and matrix[i][j] == 0:
                nm += 1
                matrix[i][j] = nm

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if i == i_max and matrix[i][j] == 0:
                nm += 1
                matrix[i][j] = nm
            elif j == j_min and i != i_max and matrix[i][j] == 0:
                nm += 1
                matrix[i][j] = nm

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end=' ')
    print()
