# раздел 18.1 экзамен Работа над файлами, задание 7* Транслитерация
with open('cyrillic.txt', 'r', encoding='utf-8') as file, open('transliteration.txt', 'w', encoding='utf-8') as trans:
    translit = {'а': 'a', 'б': 'b', 'в': 'v',
                'г': 'g', 'д': 'd', 'е': 'e',
                'ё': 'jo', 'ж': 'zh', 'з': 'z',
                'и': 'i', 'й': 'j', 'к': 'k',
                'л': 'l', 'м': 'm', 'н': 'n',
                'о': 'o', 'п': 'p', 'р': 'r',
                'с': 's', 'т': 't', 'у': 'u',
                'ф': 'f', 'х': 'h', 'ц': 'c',
                'ч': 'ch', 'ш': 'sh', 'щ': 'shh',
                'ъ': '*', 'ы': 'y', 'ь': "'",
                'э': 'je', 'ю': 'ju', 'я': 'ya'}
    data = ''
    new_data = ''
    for line in file:
        data += line

    for elem in data:
        if elem.lower() in translit:
            if elem.islower():
                new_data += translit[elem]
            else:
                new_data += translit[elem.lower()].title()
        else:
            new_data += elem

    trans.write(new_data)
