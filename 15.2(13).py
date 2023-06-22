# раздел 15.2 Функции с переменным количеством аргументов, задание 13


def greet(name, *args):
    if len(args) == 0:
        return f'Hello, {name}!'
    else:
        names = name + ' and ' + ' and '.join(args)
        return f'Hello, {names}!'


print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))
