# раздел 10.4 Задачи на словари, задание 4 Словарь синонимов
n = int(input())
dict_synonyms = {}

for _ in range(n):
    user_string = input().split()
    dict_synonyms[user_string[0]] = user_string[1]

find_word = input()

for key, value in dict_synonyms.items():
    if key == find_word:
        print(dict_synonyms[key])
    elif value == find_word:
        print(key)
