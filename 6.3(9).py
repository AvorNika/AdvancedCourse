# раздел 6.3 Основы работы с кортежами, задание 9 Конкурсный отбор
n = int(input())
rate_list = []
for _ in range(n):
    user_string = input()
    rate_list.append(user_string.split())

for i in range(n):
    print(*rate_list[i])
print()

for j in range(n):
    if rate_list[j][1] == '4' or rate_list[j][1] == '5':
        print(*rate_list[j])
