# раздел 8.6 Методы множеств, задание 14 Общие числа
string1 = set(input().split()) & set(input().split())
string2 = []
for num in string1:
    string2.append(int(num))

string2.sort()
print(*string2)
