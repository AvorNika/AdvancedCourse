# раздел 8.6 Методы множеств, задание 16 Общие цифры
n = int(input())
mylist = []
result = []
for _ in range(n):
    mylist.append(set(input()))

myset = mylist[0]
for i in range(1, len(mylist)):
    myset.intersection_update(mylist[i])

for num in myset:
    result.append(int(num))

result.sort()
print(*result)

