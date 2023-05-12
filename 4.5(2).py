# раздел 4.5 Матрицы, задание 2 Максимум в таблице
n, m = int(input()), int(input())
matrix = []
list_max = []

for _ in range(n):
    user_string = [int(num) for num in input().split()]
    matrix.append(user_string)
    list_max.append(max(user_string))

max_index = []

for i in range(n):
    if len(max_index) == 0:
        for j in range(m):
            if matrix[i][j] == max(list_max):
                max_index.append(i)
                max_index.append(j)
                print(*max_index)
                break
