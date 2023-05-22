# раздел 8.5 Методы множеств, задание 13 Количество слов в тексте
user_string = input().lower()
med_string = ''
abc = 'abcdefghijklmnopqrstuvwxyz '

for i in range(len(user_string)):
    if user_string[i] in abc:
        med_string += user_string[i]

print(len(set(med_string.split())))
