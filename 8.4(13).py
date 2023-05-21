# раздел 8.4 Основы работы с множествами, задание 13 Неповторимые цифры
user_string = input()
user_set = set(user_string)
if len(user_string) == len(user_set):
    print('YES')
else:
    print('NO')
