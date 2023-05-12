# раздел 4.5 Матрицы, задание 3 Обмен столбцов
n, m = int(input()), int(input())
matrix = []
matrix_i = []
matrix_j = []

for _ in range(n):
    user_string = [int(num) for num in input().split()]
    matrix.append(user_string)

user_numbers = input()
i, j = int(user_numbers.split()[0]), int(user_numbers.split()[1])

for a in range(n):
    for b in range(m):
        if b == i:
            matrix_i.append(matrix[a][i])
        elif b == j:
            matrix_j.append(matrix[a][j])

for r in range(n):
    for c in range(m):
        matrix[r][i], matrix[r][j] = matrix_j[r], matrix_i[r]
        print(matrix[r][c], end=' ')
    print()
