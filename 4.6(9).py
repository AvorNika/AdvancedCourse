# раздел 4.6 Матрицы, задание 9* Заполнение диагоналями
user_string = input()
n = int(user_string.split()[0])
m = int(user_string.split()[1])
matrix = [[0] * m for _ in range(n)]
numbers = [num for num in range(1, n+1)] + [num for num in range(n, 0, -1)]
nm = 0

for q in range(n+m-1):
    for i in range(n):
        for j in range(m):
            if i + j == q:
                nm += 1
                matrix[i][j] = nm

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end=' ')
    print()
