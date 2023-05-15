# раздел 4.7 Операции над матрицами в математике, задание 10* Умножение матриц
user_string_a = input()
n = int(user_string_a.split()[0])
m = int(user_string_a.split()[1])
matrix_a = []

for _ in range(n):
    user_num_a = [int(num) for num in input().split()]
    matrix_a.append(user_num_a)

input()

user_string_b = input()
m = int(user_string_b.split()[0])
k = int(user_string_b.split()[1])
matrix_b = []

for _ in range(m):
    user_num_b = [int(num) for num in input().split()]
    matrix_b.append(user_num_b)

matrix_result = [[0] * k for _ in range(n)]
matrix_m = [[0] for _ in range(m)]

for i in range(n):
    for j in range(k):
        for l in range(m):
            matrix_m[l] = matrix_a[i][l] * matrix_b[l][j]
        matrix_result[i][j] = sum(matrix_m)

for r in range(n):
    for c in range(k):
        print(matrix_result[r][c], end=' ')
    print()
