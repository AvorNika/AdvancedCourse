# раздел 11.2 экзамен, задание 4 Строка запроса
def build_query_string(user_dict):
    result = []
    for key, value in user_dict.items():
        user_str = '='.join([str(key), str(value)])
        result.append(user_str)
    return '&'.join(sorted(result))


print(build_query_string({'name': 'timur', 'age': 28}))
