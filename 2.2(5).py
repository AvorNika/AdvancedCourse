# раздел 2.2 Повторение основных конструкций, задание 5 Различные элементы
str_ = input()
new_str = str_.split()
num = []
for i in range(len(new_str)):
    if new_str[i] not in num:
        num.append(new_str[i])
print(len(num))
