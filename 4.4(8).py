# раздел 4.4 Матрицы, задание 8 Вывести матрицу 1
n = int(input())    # n - количество строк
m = int(input())   # m - количество столбцов


matrix = [[input() for _ in range(m)] for _ in range(n)]


for r in range(n):
    for c in range(m):
        print(matrix[r][c], end=' ')
    print()
