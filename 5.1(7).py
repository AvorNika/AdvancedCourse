# раздел 5.1 Итоговая работа по вложенным спискам, экзамен, задание 7 Ходы ферзя
matrix = [['.'] * 8 for _ in range(8)]
abc = 'abcdefgh'

user_value = input()
col = abc.index(user_value[0].lower())
row = 8-int(user_value[1])

for i in range(8):
    for j in range(8):
        if i == row or j == col or abs(i - row) == abs(j - col):
            matrix[i][j] = '*'
        if i == row and j == col:
            matrix[i][j] = 'Q'

for r in range(8):
    for c in range(8):
        print(matrix[r][c], end=' ')
    print()
