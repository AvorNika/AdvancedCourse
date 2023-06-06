# раздел 10.4 Задачи на словари, задание 7 Секретное слово
unknown_word = input()
n = int(input())
dict_for_decryp = {}
for _ in range(n):
    user_string = input().split(': ')
    dict_for_decryp[user_string[0]] = int(user_string[1])

decryp = {}
for elem in unknown_word:
    decryp[elem] = decryp.get(elem, 0) + 1

result = ''
for char in unknown_word:
    for key, value in dict_for_decryp.items():
        if value == decryp.get(char):
            result += key

print(result)
