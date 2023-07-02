# раздел 16.3 экзамен Функции, задание 7


def compose(func1, func2):
    def new_func(x):
        return func1(func2(x))
    return new_func


def add3(x):
    return x + 3


def mul7(x):
    return x * 7


print(compose(mul7, add3)(1))
print(compose(add3, mul7)(2))
print(compose(mul7, str)(3))
print(compose(str, mul7)(5))