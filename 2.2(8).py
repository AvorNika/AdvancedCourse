# раздел 2.2 Повторение основных конструкций, задание 8* Камень, ножницы, бумагаа, ящерица, Спок
mass = ['камень', 'ножницы', 'бумага', 'ящерица', 'спок']
str1, str2 = input().lower(), input().lower()
if str1 == str2:
    print('ничья')
elif str1 == mass[0] and str2 == mass[1] or str1 == mass[0] and str2 == mass[3] or str1 == mass[1] and str2 == mass[2] or str1 == mass[1] and str2 == mass[3] or str1 == mass[2] and str2 == mass[0] or str1 == mass[2] and str2 == mass[4] or str1 == mass[3] and str2 == mass[4] or str1 == mass[3] and str2 == mass[2] or str1 == mass[4] and str2 == mass[1] or str1 == mass[4] and str2 == mass[0]:
    print('Тимур')
else:
    print('Руслан')
    