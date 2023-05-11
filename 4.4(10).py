# раздел 4.4 Матрицы, задание 10 След матрицы
n = int(input())
matrix = []
total = 0

for _ in range(n):
    user_string = [int(num) for num in input().split()]
    matrix.append(user_string)

for i in range(n):
    for j in range(n):
        if i == j:
            total += matrix[i][i]

print(total)
