# раздел 10.3 Методы словарей, задание 11
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = {}
for elem in dict1:
    result[elem] = dict1.get(elem, 0) + dict2.get(elem, 0)

for elem in dict2:
    if elem not in result:
        result[elem] = dict2[elem]
        