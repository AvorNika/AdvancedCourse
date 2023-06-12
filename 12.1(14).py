# раздел 12.1 модуль random, задание 14
import random
ticket = set()
while len(ticket) < 7:
    ticket.add(random.randint(1, 49))

print(*sorted(ticket))
