# раздел 12.2 модуль random, задание 9
import random

tickets = set()
while len(tickets) < 100:
    ticket = ''
    for _ in range(7):
        num = random.randint(0, 9)
        ticket += str(num)
    if ticket[0] != '0':
        tickets.add(ticket)

print(*tickets, sep='\n')
print(len(tickets))
