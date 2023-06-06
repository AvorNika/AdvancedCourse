# раздел 10.4 Задачи на словари, задание 3 Анаграммы 2
string_1, string_2 = input().lower(), input().lower()   # ввод предложений для сравнения
list_1, list_2 = [], []

# убираем пробелы и знаки препинания из предложений:
for i in range(len(string_1)):
    if ord(string_1[i]) in range(97, 123) or ord(string_1[i]) in range(1072, 1104):
        list_1.append(string_1[i])

for j in range(len(string_2)):
    if ord(string_2[j]) in range(97, 123) or ord(string_2[j]) in range(1072, 1104):
        list_2.append(string_2[j])

if sorted(list_1) == sorted(list_2):
    print('YES')
else:
    print('NO')
