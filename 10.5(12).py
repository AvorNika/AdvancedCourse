# раздел 10.5 Вложенные словари и генераторы словарей, задание 12
words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

result = {word: [ord(char) for char in word] for word in words}
print(result)
