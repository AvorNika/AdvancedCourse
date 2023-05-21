# раздел 8.4 Основы работы с множествами, задание 16 Три слова
user_string = input().split()
my_set1 = set(user_string[0])
my_set2 = set(user_string[1])
my_set3 = set(user_string[2])
if my_set1 == my_set2 == my_set3:
    print('YES')
else:
    print('NO')
