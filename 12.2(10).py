# раздел 12.2 модуль random, задание 10
import random
word = list(input())
random.shuffle(word)
print(*word, sep='')
