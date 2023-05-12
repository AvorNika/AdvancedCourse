# раздел 4.5 Матрицы, задание 7 Поворот матрицы
n = int(input())
matrix = []
new_matrix = []

for _ in range(n):
    user_string = [num for num in input().split()]
    matrix.append(user_string)

matrix.reverse()

for c in range(n):
    for r in range(n):
        print(matrix[r][c], end=' ')
    print()
