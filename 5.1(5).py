# раздел 5.1 Итоговая работа по вложенным спискам, экзамен, задание 5 Симметричная матрица
n = int(input())
matrix = []
flag = True

for _ in range(n):
    user_string = [int(num) for num in input().split()]
    matrix.append(user_string)

for i in range(n):
    for j in range(n):
        if i != n - 1 - j:
            if matrix[i][j] == matrix[n - 1 - j][n - 1 - i]:
                flag = True
            else:
                flag = False
                break

if flag:
    print('YES')
else:
    print('NO')
