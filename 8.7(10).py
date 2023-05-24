# раздел 8.7 Методы множеств, задание 10 Урок информатики
score1, score2, score3 = input().split(), input().split(), input().split()


def int_score(score):
    new_score = []
    for i in range(len(score)):
        new_score.append(int(score[i]))
    return set(new_score)


new_score1 = int_score(score1)
new_score2 = int_score(score2)
new_score3 = int_score(score3)

result1 = new_score1 & new_score2
result2 = result1.difference(new_score3)

print(*sorted(result2, reverse=True))
