# раздел 10.4 Задачи на словари, задание 2 Анаграммы 1
word1, word2 = list(input()), list(input())

if sorted(word1) == sorted(word2):
    print('YES')
else:
    print('NO')
