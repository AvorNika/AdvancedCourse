# раздел 4.3 Вложенные списки, задание 9 Список по образцу 2
n = int(input())
my_list = [[j+1 for j in range(i)] for i in range(1, n+1)]
print(*my_list, sep = '\n')
