# раздел 15.4 Функции как объекты, задание 16 Интересная сортировка-2
nums = [int(num) for num in input().split()]


def sorting_sum(num):
    sum_num = 0
    for elem in str(num):
        sum_num += int(elem)
    return sum_num


nums.sort()
print(*sorted(nums, key=sorting_sum))
