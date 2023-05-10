# раздел 4.3 Вложенные списки, задание 11 Треугольник Паскаля 2
n = int(input())
import math


def pascal(num):
    for i in range(num):
        my_list = [1]
        for j in range(1, i+1):
            elem = math.factorial(i)/(math.factorial(j) * math.factorial(i-j))
            my_list.insert(j, int(elem))
        print(*my_list)


pascal(n)
