# раздел 8.5 Методы множеств, задание 12 Уникальные символы 2
n = int(input())
result = ''

for _ in range(n):
    result += input().lower()

print(len(set(result)))
