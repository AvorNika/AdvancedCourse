# раздел 5.1 Итоговая работа по вложенным спискам, экзамен, задание 6* Латинский квадрат
n = int(input())
check_matrix = [i for i in range(1, n + 1)]
matrix = []
counter = 0

for _ in range(n):
    user_string = [int(num) for num in input().split()]
    matrix.append(user_string)


def function(user_list):
    user_list.sort()
    if user_list == check_matrix:
        return True
    else:
        return False


new_matrix = []
for j in range(n):
    new = []
    for i in range(n):
        new.append(matrix[i][j])
    new_matrix.append(new)

for r in range(n):
    counter += function(matrix[r])

for c in range(n):
    counter += function(new_matrix[c])

if counter == n * 2:
    print('YES')
else:
    print('NO')
