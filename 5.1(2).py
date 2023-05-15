# раздел 5.1 итоговая работа по вложенным спискам, экзамен, задание 2 Максимальный в области 2
n = int(input())
matrix = []

for _ in range(n):
    user_string = [int(num) for num in input().split()]
    matrix.append(user_string)

max_num = matrix[n-1][n-1]

for i in range(n):
    for j in range(n):
        if i >= n - 1 - j:
            if matrix[i][j] > max_num:
                max_num = matrix[i][j]

print(max_num)
