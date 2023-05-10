# раздел 2.1 Повторение основных конструкций, задание 8 Standard American Convention
number = input()
new_number = ''
len_number = len(number)
if len_number < 4:
    print(number)
else:
    number_int = number[::-1]
    for i in range(len(number_int)):
        new_number += number_int[i]
        if (i+1) % 3 == 0 and i+1 < len(number_int):
            new_number += ','
    print(new_number[::-1])
    