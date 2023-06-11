# раздел 10.5 Вложенные словари и генераторы словарей, задание 10
# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
# s1 = s.split()
# s2 = []
# for elem in s1:
#     num = ''
#     word = ''
#     for char in elem:
#         if char.isdigit():
#             num += char
#         if char.isalpha():
#             word += char
#     s2.append((int(num), word))
# print(s2)
# result = dict(s2)
# print(result)

s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'

result = {int(elem.split(':')[0]): elem.split(':')[1] for elem in s.split()}
print(result)
