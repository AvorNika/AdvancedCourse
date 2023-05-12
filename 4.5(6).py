# раздел 4.5 Матрицы, задание 6 Зеркальное отображение
n = int(input())
matrix = []

for _ in range(n):
    user_string = [num for num in input().split()]
    matrix.insert(0, user_string)

for r in range(n):
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()
