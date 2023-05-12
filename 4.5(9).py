# раздел 4.5 Матрицы, задание 9* Магический квадрат
n = int(input())
matrix = []
matrix_main = []
matrix_side = []
check_number = [v for v in range(1, n**2+1)]
matrix_check = []
flag = True

for _ in range(n):   # создаём матрицу
    user_string = [int(num) for num in input().split()]
    matrix.append(user_string)
    matrix_check.extend(user_string)

matrix_check.sort()
if matrix_check != check_number:   # проверка чисел на соответствие условию
    flag = False

total = sum(matrix[0])

for r in range(n):   # проверяем строки на соответствие условию
    if sum(matrix[r]) != total:
        flag = False
        break

for a in range(n):
    for b in range(n):
        if a == b:
            matrix_main.append(matrix[a][a])
if sum(matrix_main) != total:   # проверяем главную диагональ на соответствие условию
    flag = False

for k in range(n):
    for l in range(n):
        if k == l:
            matrix_side.append(matrix[l][n-l-1])
if sum(matrix_side) != total:   # проверяем побочную диагональ на соответствие условию
    flag = False

matrix.reverse()
new_matrix = [[] for _ in range(n)]
for j in range(n):
    for i in range(n):
        new_matrix[j].append(matrix[i][j])

for c in range(n):   # проверяем столбцы на соответствие условию
    if sum(new_matrix[c]) != total:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')
