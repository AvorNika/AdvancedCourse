# раздел 15.8 Анонимные функции, задание 6
func = lambda s: s[0].lower() == 'a' and s[-1].lower() == 'a'

print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))

