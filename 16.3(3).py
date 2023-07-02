# раздел 16.3 экзамен Функции, задание 3
words = 'the world is mine take a look what you have started'.split()

print(*list(map(lambda x: '"' + x + '"', words)))
