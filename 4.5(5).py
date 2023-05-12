# раздел 4.5 Матрицы, задание 5 Обмен диагоналей
n = int(input())
matrix = []
matrix_main = []
matrix_side = []

for _ in range(n):
    user_string = [int(num) for num in input().split()]
    matrix.append(user_string)

for a in range(n):
    for b in range(n):
        if a == b:
            matrix_main.append(matrix[a][a])

for k in range(n):
    for l in range(n):
        if k == l:
            matrix_side.append(matrix[l][n-l-1])

matrix_side.reverse()

for r in range(n):
    for c in range(n):
        matrix[r][r], matrix[n-c-1][c] = matrix_side[c], matrix_main[c]
        print(matrix[r][c], end=' ')
    print()
