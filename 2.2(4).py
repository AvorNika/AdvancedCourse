# раздел 2.2 Повторение основных конструкций, задание 4 Сдвиг в развитии
str_ = input()
new_str = str_.split()
new_str.insert(0, new_str.pop(-1))
print(*new_str)
