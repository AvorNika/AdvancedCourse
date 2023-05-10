# раздел 4.3 Вложенные списки, задание 14** Подсписки списка
str1 = input()


def str_str(string):
    new_str = string.split()
    result = [[]]
    mid_str = []
    for i in range(len(new_str)):
        result.append([new_str[i]])
    len_all = (len(new_str)**2+1)-0.5*(len(new_str)*(len(new_str)-1))
    while len(result) < int(len_all):
        for dl in range(2, len(new_str)+1):
            mid_str = []
            for j in range(len(new_str)-1):
                mid_str.append(new_str[j])
                for k in range(j+1, len(new_str)):
                    mid_str.append(new_str[k])
                    if len(mid_str) < dl:
                        continue
                    elif len(mid_str) == dl and ''.join(mid_str) in ''.join(new_str):
                        result.append(mid_str)
                        mid_str = []
                        break

    return result


print(str_str(str1))
