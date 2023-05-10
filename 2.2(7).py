# раздел 2.2 Повторение основных конструкций, задание 7 Камень, ножницы, бумага
mass = ['камень', 'ножницы', 'бумага']
str1, str2 = input().lower(), input().lower()
if str1 == mass[0] and str2 == mass[1] or str1 == mass[1] and str2 == mass[2] or str1 == mass[2] and str2 == mass[0]:
    print('Тимур')
elif str2 == mass[0] and str1 == mass[1] or str2 == mass[1] and str1 == mass[2] or str2 == mass[2] and str1 == mass[0]:
    print('Руслан')
elif str1 == str2:
    print('ничья')
    