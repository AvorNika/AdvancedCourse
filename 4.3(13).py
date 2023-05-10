# раздел 4.3 Вложенные списки, задание 13* Разбиение на чанки
str1 = input()
str2 = int(input())

def chunked(string, num):
    new_str = string.split()
    mid_str = []
    result = []
    for i in range(len(new_str)):
        if len(mid_str) < num:
            mid_str.extend(new_str[i])
            if i == len(new_str)-1:
                result.append(mid_str)
        elif len(mid_str) == num:
            result.append(mid_str)
            mid_str = []
            mid_str.extend(new_str[i])
            if i == len(new_str)-1:
                result.append(mid_str)

    return result


print(chunked(str1, str2))
