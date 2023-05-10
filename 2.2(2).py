# раздел 2.2 Повторение основных конструкций, задание 2 Больше предыдущего
str_ = input()
new_str = str_.split()
a = int(new_str[0])
counter = 0
for i in range(len(new_str)):
    if int(new_str[i]) > a:
        counter += 1
    a = int(new_str[i])
print(counter)
