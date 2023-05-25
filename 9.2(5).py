# раздел 9.2 экзамен, Множества, задание 5 Книги на прочтение
m, n = int(input()), int(input())
home_books = set()
list_for_summer = []

for _ in range(m):
    home_books.add(input().lower())

for _ in range(n):
    list_for_summer.append(input().lower())

for book in list_for_summer:
    if book.lower() in home_books:
        print('YES')
    else:
        print('NO')
