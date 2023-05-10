# раздел 2.2 Повторение основных конструкций, задание 11** Роскомнадзор запретил букву а
word = input() + ' запретил букву'
alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'


def function(string):
    for i in range(len(alphabet)):
        new_string = ''
        if alphabet[i] in string:
            print(string.strip(), alphabet[i])
            for j in range(len(string)):
                if string[j] != alphabet[i]:
                    new_string += string[j]
        else:
            continue
        if '  ' in new_string:
            mid_string = new_string.split()
            string = ''
            for k in range(len(mid_string)):
                string += (mid_string[k] + ' ')
        else:
            string = new_string


function(word)
