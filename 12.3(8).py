# раздел 12.3 Метод Монте-Карло и Bogosort
import random
s0 = 4
k = 0
n = 10**6

for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        k += 1

s = k / n * s0
print(s)
