# раздел 12.2 модуль random, задание 8
import random

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

list_m = []

for i in range(4):
    for j in range(4):
        list_m.append(matrix[i][j])

random.shuffle(list_m)


matrix_m = [[0]*4 for _ in range(4)]
for k in range(4):
    for l in range(4):
        matrix_m[k][l] = list_m[4*k+l]

print(matrix_m)
