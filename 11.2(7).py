# раздел 11.2 экзамен, задание 7* Покупки в интернет-магазине
n = int(input())

customers = {}
for _ in range(n):
    user_str = input().split()
    name, supply, counter = user_str[0], user_str[1], int(user_str[2])
    if customers.get(name) is None:
        customers[name] = {supply: counter}
    else:
        if customers[name].get(supply) is None:
            customers[name][supply] = counter
        else:
            customers[name][supply] += counter


new_dict = []
for key, value in customers.items():
    new_res = []
    for k, v in value.items():
        new_res.append([k, v])
        new_res.sort()
    new_dict.append([key, new_res])
new_dict.sort()

for i in range(len(new_dict)):
    print(f'{new_dict[i][0]}:')
    for j in range(len(new_dict[i][1])):
        print(*new_dict[i][1][j])
