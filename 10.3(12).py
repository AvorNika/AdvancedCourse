# раздел 10.3 Методы словарей, задание 12
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}

for elem in text:
    result[elem] = result.get(elem, 0) + 1
