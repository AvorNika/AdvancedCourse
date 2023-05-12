# раздел 4.5 Матрицы, задание 4 Симметричная матрица
n = int(input())
matrix = []
flag = True

for _ in range(n):
    user_string = [int(num) for num in input().split()]
    matrix.append(user_string)

for r in range(n):
    for c in range(n):
        if r != c:
            if matrix[r][c] != matrix[c][r]:
                flag = False

if flag:
    print('YES')
else:
    print('NO')
