# раздел 10.2 Основы работы со словарями, задание 15 Набор сообщений
user_string = input().upper()
result = ''
phone = {1: '.,?!:',
         2: 'ABC',
         3: 'DEF',
         4: 'GHI',
         5: 'JKL',
         6: 'MNO',
         7: 'PQRS',
         8: 'TUV',
         9: 'WXYZ',
         0: ' '}

for i in range(len(user_string)):
    for num in phone:
        if user_string[i] in phone[num]:
            result += (str(num) * (phone[num].index(user_string[i]) + 1))

print(result)
