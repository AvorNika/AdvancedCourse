# раздел 2.2 Повторение основных конструкций, задание 1 Координатные четверти
n = int(input())
counter1, counter2, counter3, counter4 = 0, 0, 0, 0
for i in range(n):
    str_ = input()
    new_str = str_.split()
    x, y = int(new_str[0]), int(new_str[1])
    if x > 0 and y > 0:
        counter1 += 1
    elif x < 0 and y > 0:
        counter2 += 1
    elif x < 0 and y < 0:
        counter3 += 1
    elif x > 0 and y < 0:
        counter4 += 1

print('Первая четверть:', counter1)
print('Вторая четверть:', counter2)
print('Третья четверть:', counter3)
print('Четвертая четверть:', counter4)
