# раздел 9.2 экзамен, Множества, задание 4 Города
n = int(input())
list_of_cities = set()
for _ in range(n):
    list_of_cities.add(input().lower())

user_city = input()
if user_city.lower() in list_of_cities:
    print('REPEAT')
else:
    print('OK')
