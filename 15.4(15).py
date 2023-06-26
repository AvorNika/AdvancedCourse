# раздел 15.4 Функции как объекты, задание 15 Интересная сортировка-1
nums = input().split()


def sorting_sum(num):
    sum_num = 0
    for elem in num:
        sum_num += int(elem)
    return sum_num


print(*sorted(nums, key=sorting_sum))
