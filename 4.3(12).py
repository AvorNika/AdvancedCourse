# раздел 4.3 Вложенные списки, задание 12* Упаковка дубликатов
str1 = input()
new_str = str1.split()
result = []
mid_str = []
for i in range(len(new_str)):
    if len(mid_str) == 0:
        mid_str.extend(new_str[i])
        if i == len(new_str)-1:
            result.append(mid_str)
    else:
        if new_str[i] in mid_str:
            mid_str.extend(new_str[i])
            if i == len(new_str) - 1:
                result.append(mid_str)
        else:
            result.append(mid_str)
            mid_str = []
            mid_str.extend(new_str[i])
            if i == len(new_str) - 1:
                result.append(mid_str)

print(result)
