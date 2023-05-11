# раздел 4.4 Матрицы, задание 14 Суммы четвертей
n = int(input())
matrix = []
list_total = [[], [], [], []]

for _ in range(n):
    user_string = [int(num) for num in input().split()]
    matrix.append(user_string)


for i in range(n):
    for j in range(n):
        if i < j and i < n-1-j:
            list_total[0].append(matrix[i][j])

        elif i < j and i > n - 1 - j:
            list_total[1].append(matrix[i][j])

        elif i > j and i > n - 1 - j:
            list_total[2].append(matrix[i][j])

        elif i > j and i < n - 1 - j:
            list_total[3].append(matrix[i][j])


print('Верхняя четверть:', sum(list_total[0]))
print('Правая четверть:', sum(list_total[1]))
print('Нижняя четверть:', sum(list_total[2]))
print('Левая четверть:', sum(list_total[3]))
