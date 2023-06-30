# раздел 15.8 Анонимные функции, задание 15 Противоположный цвет
RGB = [int(i) for i in input().split()]

NegRGB = list(map(lambda color: 255 - color, RGB))

print(*NegRGB)
