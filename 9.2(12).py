# раздел 9.2 экзамен, Множества, задание 12* Онлайн-школа BEEGEEK 6
m = int(input())
list_of_all = []

for i in range(m):
    n = int(input())
    list_of_students = set()
    for j in range(n):
        list_of_students.add(input())

    list_of_all.append(list_of_students)

result = list_of_all[0]
for k in range(1, m):
    result.intersection_update(list_of_all[k])

print(*sorted(result), sep='\n')
