# раздел 11.2 экзамен, задание 1 Минутка генетики
DNA = ['G', 'C', 'T', 'A']
RNA = ['C', 'G', 'A', 'U']

convert = dict(zip(DNA, RNA))

user_string = input()
# new_string = ''
# for elem in user_string:
#     new_string += convert[elem]
#print(new_string)

print(*[convert[elem] for elem in user_string], sep='')
