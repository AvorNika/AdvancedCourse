# раздел 10.4 Задачи на словари, задание 1 Словарь программиста
n = int(input())   # количество слов в словаре
prog_dict = {}

for _ in range(n):   # добавляем вводимые пользователем слова и их определения в словарь
    user_string = input()
    key = user_string[:user_string.index(':')].lower()
    prog_dict[key] = user_string[user_string.index(':')+2:]

m = int(input())   # количество поисковых слов, которые нужно вывести

print_words = []

for _ in range(m):   # создаем список слов, чьи определения нужно вывести
    user_word = input().lower()
    print_words.append(user_word)

for word in print_words:
    print(prog_dict.get(word, 'Не найдено'))
