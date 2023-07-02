# раздел 15.9 Встроенные функции any(), all(), zip(), enumerate(), задание 11 Корректный IP-адрес
address = [i for i in input().split('.')]

result = all(map(lambda y: 0 <= y <= 255, map(lambda x: int(x) if x.isdigit() else 256, address)))
print(result)
