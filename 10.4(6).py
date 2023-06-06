# раздел 10.4 Задачи на словари, задание 6 Телефонная книга
n = int(input())
phonebook = {}

for _ in range(n):
    user_string = input().lower().split()
    if user_string[1] not in phonebook:
        phonebook[user_string[1]] = [user_string[0]]
    else:
        phonebook[user_string[1]].append(user_string[0])

m = int(input())
requests = [input().lower() for _ in range(m)]

for name in requests:
    print(*phonebook.get(name, ['абонент не найден']))
