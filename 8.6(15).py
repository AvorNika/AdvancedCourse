# раздел 8.6 Методы множеств, задание 15 Числа первой строки
string1 = set(input().split()) - set(input().split())
string2 = []
for num in string1:
    string2.append(int(num))
string2.sort()
print(*string2)
