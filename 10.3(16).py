# раздел 10.3 Методы словарей, задание 16* Исправление дубликатов
user_string = input().split()

result = {}
new_result = []

for word in user_string:
    result[word] = result.get(word, 0) + 1
    if result[word] == 1:
        new_result.append(word)
    else:
        new_result.append(f'{word}_{result[word]-1}')

print(*new_result)
