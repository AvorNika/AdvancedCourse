# раздел 15.9 Встроенные функции any(), all(), zip(), enumerate(), задание 8
def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    result = any(map(lambda word: word in command, ignore))
    return result


# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
#
#     for word in ignore:
#         if word in command:
#             return True
#     return False


print(ignore_command('get ip'))
print(ignore_command('select all'))
print(ignore_command('delete'))
print(ignore_command('trancate'))
