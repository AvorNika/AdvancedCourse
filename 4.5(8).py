# раздел 4.5 Матрицы, задание 8 Ходы коня
matrix = [['.'] * 8 for _ in range(8)]
abc = 'abcdefgh'

user_value = input()
col = abc.index(user_value[0].lower())
row = 8-int(user_value[1])

for i in range(8):
    for j in range(8):
        if i == row and j == col:
            matrix[i][j] = 'N'
        if i == row + 2 and j == col - 1 or i == row + 2 and j == col + 1 or i == row - 2 and j == col + 1 or i == row - 2 and j == col - 1 or i == row + 1 and j == col + 2 or i == row + 1 and j == col - 2 or i == row - 1 and j == col + 2 or i == row - 1 and j == col - 2:
            matrix[i][j] = '*'

for r in range(8):
    for c in range(8):
        print(matrix[r][c], end=' ')
    print()
