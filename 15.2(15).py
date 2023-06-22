# раздел 15.2 Функции с переменным количеством аргументов, задание 15


def info_kwargs(**kwargs):
    for key, value in sorted(kwargs.items()):
        print(f'{key}: {value}')


info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
