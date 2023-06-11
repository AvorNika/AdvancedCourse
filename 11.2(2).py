# раздел 11.2 экзамен, задание 2 Порядковый номер
user_string = input().split()
my_dict = {}
for word in user_string:
    my_dict[word] = my_dict.get(word, 0) + 1
    print(my_dict[word], end=' ')
