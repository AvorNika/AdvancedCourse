# раздел 10.3 Методы словарей, задание 13
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
list1 = s.split()
result = {}
new_result = {}

for elem in list1:
    result[elem] = result.get(elem, 0) + 1

for key, value in result.items():
    if value == max(result.values()):
        new_result[key] = value

print(min(new_result))
