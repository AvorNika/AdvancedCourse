# раздел 16.3 экзамен Функции, задание 10 Гематрия слова
n = int(input())
words = [input() for _ in range(n)]


def is_ord(w):
    result = sum(map(lambda x: (ord(x.upper()) - ord('A')), w))
    return result


res = sorted(sorted(words), key=is_ord)

print(*res, sep='\n')
