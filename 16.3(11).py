# раздел 16.3 экзамен Функции, задание 11 Сортировка IP-адресов
n = int(input())
ip_addresses = [input() for _ in range(n)]


def is_sum(address):
    addr = address.split('.')
    addr_ind = [i for i in range(len(addr))]
    res = sum(map(lambda x, y: int(x) * 256 ** y, addr, addr_ind[::-1]))
    return res


result = sorted(sorted(ip_addresses), key=is_sum)

print(*result, sep='\n')
