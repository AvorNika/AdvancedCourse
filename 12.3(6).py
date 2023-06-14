# раздел 12.3 Метод Монте_карло и Bogosort
import random
s0 = 16
k = 0
n = 10**6   # количество испытаний

for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    if x**3 + y**4 + 2 >= 0 and 3*x + y**2 <= 2:
        k += 1

s = k / n * s0
print(s)
