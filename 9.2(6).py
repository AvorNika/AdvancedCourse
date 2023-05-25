# раздел 9.2 экзамен, задание 6 Странное увлечение
set1 = {int(i) for i in input().split()}
set2 = {int(i) for i in input().split()}

if set1.isdisjoint(set2):
    print('BAD DAY')
else:
    print(*sorted(set1.intersection(set2), reverse=True))
