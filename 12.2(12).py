# раздел 12.2 модуль random, задание 12* Тайный друг
import random
n = int(input())   # количество учеников
students = []   # список всех учеников

result = {}   # итоговые пары друзей
for _ in range(n):
    user_string = input()
    students.append(user_string)   # собираем учеников в список

friends = students.copy()   # список тайных друзей

for student in students:   # перебираем всех учеников
    friend = random.choice(friends)   # выбираем случайного тайного друга
    if friend == student:   # если выпало, что студент является сам себе тайным другом
        del friends[friends.index(student)]   # удаляем студента из списка возможных тайных друзей
        new_friend = random.choice(friends)   # выбираем нового тайного друга
        result[student] = new_friend   # добавляем пару друзей в итоговый список пар
        del friends[friends.index(new_friend)]   # удаляем нового тайного друга из списка тайных друзей
        friends.append(student)
    else:
        result[student] = friend   # добавляем ученика и его тайного друга в итоговые пары друзей
        del friends[friends.index(friend)]   # добавляем тайного друга в список занятых тайных друзей

for key, value in result.items():
    print(f'{key} - {value}')
