# раздел 2.2 Повторение основных конструкций, задание 10** Кремниевая долина
n = int(input())
mass = [input() for i in range(n)]
counter = []
def function_(string):
    word = ['a', 'n', 't', 'o', 'n']
    result = []
    new_string = list(string)
    for i in range(len(word)):
        if word[i] in new_string:
            result.append(word[i])
            del new_string[:new_string.index(word[i])+1]
        else:
            break
    if result == word and len(result) == 5:
        return 1
    else:
        return 0


for i in range(len(mass)):
    a = function_(mass[i])
    if a > 0:
        counter.append(i+1)

print(*counter)
