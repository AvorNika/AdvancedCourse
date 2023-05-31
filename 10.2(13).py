# раздел 10.2 Основы работы со словарями, задание 13 Строковое представление
n = int(input())
my_dict = {'0': 'zero',
           '1': 'one',
           '2': 'two',
           '3': 'three',
           '4': 'four',
           '5': 'five',
           '6': 'six',
           '7': 'seven',
           '8': 'eight',
           '9': 'nine'}

result = []
for i in range(len(str(n))):
    result.append(my_dict[str(n)[i]])

print(*result)
