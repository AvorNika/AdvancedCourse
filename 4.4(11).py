# раздел 4.4 Матрицы, задание 11 Больше среднего
n = int(input())
matrix = []
list_average = []

for _ in range(n):
    user_string = [int(num) for num in input().split()]
    list_average.append(sum(user_string)/n)
    matrix.append(user_string)

for i in range(n):
    counter = 0
    for j in range(n):
        if matrix[i][j] > list_average[i]:
            counter += 1
    print(counter)
