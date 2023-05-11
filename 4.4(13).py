# раздел 4.4 Матрицы, задание 13* Максимальный в области 2
n = int(input())
matrix = []

for _ in range(n):
    user_string = [int(num) for num in input().split()]
    matrix.append(user_string)

max_number = matrix[0][0]

for i in range(n):
    for j in range(n):
        if i >= j and i <= n-1-j or i <= j and i >= n-1-j:
            if matrix[i][j] > max_number:
                max_number = matrix[i][j]

print(max_number)
