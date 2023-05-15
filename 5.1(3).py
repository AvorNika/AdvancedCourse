# раздел 5.1 Итоговая работа по вложенным спискам, экзамен, задание 3 Транспонирование матрицы
n = int(input())
matrix = []

for _ in range(n):
    user_string = [num for num in input().split()]
    matrix.append(user_string)

for c in range(n):
    for r in range(n):
        print(matrix[r][c], end=' ')
    print()
