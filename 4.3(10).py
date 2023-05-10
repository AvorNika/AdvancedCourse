# раздел 4.3 Вложенные списки, задание 10* Треугольник Паскаля
n = int(input())
my_list = [1]
import math


def pascal(num):
    for i in range(1, num+1):
        elem = math.factorial(num)/(math.factorial(i) * math.factorial(num-i))
        my_list.insert(i, int(elem))
    return my_list


print(pascal(n))
