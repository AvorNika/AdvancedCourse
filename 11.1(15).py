# раздел 11.1 экзамен, задание 15
emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}

result = [elem + '@' + key for key, value in emails.items() for elem in value]

# result = []
# for key, value in emails.items():
#     for elem in value:
#         result.append(elem+'@'+key)

print(*sorted(result), sep='\n')
