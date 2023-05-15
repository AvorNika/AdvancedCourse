# раздел 4.7 Операции над матрицами в математике, задание 9 Сложение матриц
user_string = input()
n = int(user_string.split()[0])
m = int(user_string.split()[1])
matrix_a = []
matrix_b = []
matrix_result = [[0] * m for _ in range(n)]

for _ in range(n):
    user_num_a = [int(num) for num in input().split()]
    matrix_a.append(user_num_a)

input()

for _ in range(n):
    user_num_b = [int(num) for num in input().split()]
    matrix_b.append(user_num_b)

for i in range(n):
    for j in range(m):
        matrix_result[i][j] = matrix_a[i][j] + matrix_b[i][j]

for r in range(n):
    for c in range(m):
        print(matrix_result[r][c], end=' ')
    print()
