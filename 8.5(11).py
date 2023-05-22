# раздел 8.5 Методы множеств, задание 11 Уникальные символы 1
n = int(input())
result = []

for _ in range(n):
    result.append(len(set(input().lower())))

print(*result, sep='\n')
