# раздел 15.4 Функции как объекты, задание 14 Математические функции
import math
num = int(input())
operation = input()

criteria = {'квадрат': num**2, 'куб': num**3, 'корень': math.sqrt(abs(num)), 'модуль': abs(num), 'синус': math.sin(num)}
print(criteria[operation.lower()])
