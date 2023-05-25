# раздел 9.2 экзамен, Множества, задание 10 Онлайн-школа BEEGEEK 4
list_dir = {i for i in input().split()}
list_help = {i for i in input().split()}

list_of_all = list_dir.union(list_help)

print(*sorted(list_of_all))
