# раздел 10.3 Методы словарей, задание 15* Самое редкое слово
user_string = input().lower()
string1 = []

for i in range(len(user_string)):
    if user_string[i] not in '.,!?;:-':
        string1 += user_string[i]

new_string = ''.join(string1).split()

result = {}
new_result = []

for word in new_string:
    result[word] = result.get(word, 0) + 1

for key, value in result.items():
    if value == min(result.values()):
        new_result.append(key)

print(min(new_result))
