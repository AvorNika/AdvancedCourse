# раздел 13.1 Модуль decimal, задание 12
from decimal import *
num = Decimal(input())
nums = num.as_tuple().digits
if 0 < abs(num) < 1:
    nums += (0, )
print(min(nums) + max(nums))
