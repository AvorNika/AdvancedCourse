# раздел 15.1 Необязательные и именованные аргументы, задание 16
def matrix(n=1, m=None, value=0):
    if m is None:
        matrix1 = [[value] * n for _ in range(n)]
    else:
        matrix1 = [[value] * m for _ in range(n)]
    return matrix1


print(matrix(3, 4, 9))
