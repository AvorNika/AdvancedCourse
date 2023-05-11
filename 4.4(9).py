# раздел 4.4 Матрицы, задание 9 Вывести матрицу 2
n = int(input())    # n - количество строк
m = int(input())   # m - количество столбцов


matrix = [[input() for _ in range(m)] for _ in range(n)]


for r in range(n):
    for c in range(m):
        print(matrix[r][c], end=' ')
    print()

print()

for c in range(m):
    for r in range(n):
        print(matrix[r][c], end=' ')
    print()
