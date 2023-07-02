# раздел 15.9 Встроенные функции any(), all(), zip(), enumerate(), задание 14 Отличники
n = int(input())
all_students = []

for _ in range(n):
    k = int(input())
    students = {}
    for _ in range(k):
        user_string = input().split()
        med = students.setdefault(user_string[0], int(user_string[1]))
    all_students.append(students)

result = all(map(lambda s: 5 in s.values(), all_students))

if result:
    print('YES')
else:
    print('NO')
