# раздел 12.1 модуль random, задание 13
import random
n = int(input())   # длина пароля
password = []
while len(password) < n:
    password += chr(random.randint(65, 90))
    password += chr(random.randint(97, 122))

random.shuffle(password)

if len(password) > n:
    del password[-1]

print(*password, sep='')
