# раздел 15.9 Встроенные функции any(), all(), zip()m enumerate(), задание 13 Хороший пароль
password = input()

result = all([any(map(lambda a: a.isdigit(), password)), any(map(lambda b: b.islower(), password)), any(map(lambda c: c.isupper(), password)), len(password) >= 7])

if result:
    print('YES')
else:
    print('NO')
