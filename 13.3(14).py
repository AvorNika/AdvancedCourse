# раздел 13.3 Тип данных complex, задание 14 Сопряжённые числа
n = int(input())
z1, z2 = complex(input()), complex(input())
result = z1**n + z2**n + z1.conjugate()**n + z2.conjugate()**(n + 1)
print(result)
