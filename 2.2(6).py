# раздел 2.2 Повторение основных конструкций, задание 6 Произведение чисел
n = int(input())
num = [int(input()) for i in range(n)]
x = int(input())
counter = 0
for j in range(n):
    for k in range(n):
        if num[j] * num[k] == x and j != k:
            counter += 1
if counter > 0:
    print('ДА')
else:
    print('НЕТ')
    