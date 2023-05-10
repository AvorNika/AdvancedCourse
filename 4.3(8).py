# раздел 4.3 Вложенные списки, задание 8 Список по образцу 1
n = int(input())
my_list = [[i for i in range(1, n+1)] for _ in range(n)]
print(*my_list, sep = '\n')
