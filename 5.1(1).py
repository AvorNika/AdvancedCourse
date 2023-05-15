# раздел 5.1 Итоговая работа по вложенным спискам, экзамен, задание 1 Каждый n-ый элемент
user_string = input()
n = int(input())

user_list = user_string.split()
result_list = [[] for _ in range(n)]

while len(user_list) > 0 and len(user_list) >= n:
    new_list = user_list[:n]
    del user_list[:n]
    for i in range(n):
        result_list[i].append(new_list[i])

if n > len(user_list) > 0:
    new_list = user_list
    for j in range(len(user_list)):
        result_list[j].append(new_list[j])

print(result_list)
