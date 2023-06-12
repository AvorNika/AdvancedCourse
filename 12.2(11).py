# раздел 12.2 модуль random, задание 11
import random
card = [[0]*5 for _ in range(5)]
numbers = set()
while len(numbers) < 25:
    numbers.add(random.randint(1, 75))

numbers = list(numbers)
for i in range(5):
    for j in range(5):
        card[i][j] = numbers[i*5+j]

card[2][2] = 0

for r in range(5):
    for c in range(5):
        print(str(card[r][c]).ljust(3), end='')
    print()
