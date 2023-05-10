# раздел 2.2 Повторение основных конструкций, задание 9 Орёл и решка
str_ = input()
mass = []
counter = 0
for i in range(len(str_)):
    if str_[i] == 'Р':
        counter += 1
    else:
        counter = 0
    mass.append(counter)
print(max(mass))
