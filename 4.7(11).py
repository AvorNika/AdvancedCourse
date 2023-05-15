# раздел 4.7 Операции над матрицами в математике, задание 11* Возведение матрицы в степень
n = int(input())
matrix_user = []
counter = 1

for _ in range(n):
    user_string = [int(num) for num in input().split()]
    matrix_user.append(user_string)

m = int(input())


def function(matrix_f):
    matrix_m = [[0] for _ in range(n)]
    matrix_result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for p in range(n):
                matrix_m[p] = matrix_f[i][p] * matrix_user[p][j]
            matrix_result[i][j] = sum(matrix_m)
    return matrix_result


matrix_copy = matrix_user[:]
new_matrix = function(matrix_copy)
counter += 1
while counter < m:
    matrix_copy = new_matrix[:]
    new_matrix = function(matrix_copy)
    counter += 1

for r in range(n):
    for c in range(n):
        print(new_matrix[r][c], end=' ')
    print()
