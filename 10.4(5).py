# раздел 10.4 Задачи на словари, задание 5 Страны и города
n = int(input())
dict_cities = {}

for _ in range(n):
    user_string = input().split()
    dict_cities[user_string[0]] = user_string[1:]

m = int(input())
cities = [input() for _ in range(m)]

for city in cities:
    for key, value in dict_cities.items():
        if city in value:
            print(key)
