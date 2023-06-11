# раздел 11.2 экзамен, задание 6 Опасный вирус
my_dict = {'write': 'W', 'read': 'R', 'execute': 'X'}   # расшифровка операций

n = int(input())   # количество файлов в системе
files = {}   # словарь файлов и разрешённых операций с ними
for _ in range(n):
    user_string = input().split()
    files[user_string[0]] = user_string[1:]

m = int(input())    # количество запросов
queries = []
queries_operations = []
for _ in range(m):
    user_str = input().split()
    queries.append(user_str[1])   # формируем список запросов файлов
    queries_operations.append(user_str[0])   # формируем список операций с файлами

for i in range(len(queries)):
    if my_dict[queries_operations[i]] in files[queries[i]]:
        print('OK')
    else:
        print('Access denied')
