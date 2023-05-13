# раздел 4.6 Матрицы, задание 7* Заполнение 5
user_string = input()
n = int(user_string.split()[0])
m = int(user_string.split()[1])
matrix = [[0] * m for _ in range(n)]
numbers = [num for num in range(1, m+1)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = numbers[j]
    new_number = numbers.pop(0)
    numbers.append(new_number)

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end=' ')
    print()
