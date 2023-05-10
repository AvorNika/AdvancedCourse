# раздел 2.1 Повторение основных конструкций, задание 3 Индекс массы тела
weight, length = float(input()), float(input())
IMT = weight/(length**2)
if IMT < 18.5:
    print('Недостаточная масса')
elif IMT > 25:
    print('Избыточная масса')
else:
    print('Оптимальная масса')
    