# раздел 11.2 экзамен, задание 3 Scrabble game
score = {1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
         2: ['D', 'G'],
         3: ['B', 'C', 'M', 'P'],
         4: ['F', 'H', 'V', 'W', 'Y'],
         5: ['K'],
         8: ['J', 'X'],
         10: ['Q', 'Z']}

user_word = input().upper()
counter = 0

for key, value in score.items():
    for char in user_word:
        if char in value:
            counter += key

print(counter)
