# раздел 2.1 Повторение основных конструкций, задание 7 Переворот числа
num = input()
new_num = []
ready_num = []


for j in range(len(num)):
    new_num += num[j]

if len(new_num) == 6:
    ready_num += new_num[0]
    del new_num[0]
    new_num.reverse()
    for j in range(len(new_num)):
        ready_num += new_num[j]

elif len(new_num) == 5:
    new_num.reverse()
    for k in range(len(new_num)):
        ready_num += new_num[k]

while ready_num[0] == '0':
    if ready_num[0] == '0':
        del ready_num[0]

final = ''.join(ready_num)
print(final)
