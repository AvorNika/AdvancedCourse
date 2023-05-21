# раздел 8.4 Основы работы с множествами, задание 14 Все 10 цифр
my_set1 = set(input())
my_set2 = set(input())
result = []
for num in my_set1:
    if num not in result:
        result.append(num)

for num in my_set2:
    if num not in result:
        result.append(num)

if len(result) == 10:
    print('YES')
else:
    print('NO')
