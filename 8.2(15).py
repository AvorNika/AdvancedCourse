# раздел 8.2 Операции над множествами, диаграммы Эйлера-Венна, задание 15* Книги на прочтение
n, m, k, x, y, z, t, a = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
read_one = 3 * (t - n - m - k) + 2 * (x + y + z)
read_two = 2 * (n + m + k) - 3 * t - x - y - z
read_null = a - read_one - read_two - t
print(read_one)
print(read_two)
print(read_null)
