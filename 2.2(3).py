# раздел 2.2 Повторение основных конструкций, задание 3 Назад, вперёд и наоборот
str_ = input()
new_str = str_.split()
result = []
if len(new_str) % 2 == 0:
    while len(new_str) > 0:
        result.append(new_str[1])
        result.append(new_str[0])
        del new_str[:2]
elif len(new_str) % 2 == 1:
    while len(new_str) > 1:
        result.append(new_str[1])
        result.append(new_str[0])
        del new_str[:2]
    else:
        result.append(new_str[0])

print(*result)
