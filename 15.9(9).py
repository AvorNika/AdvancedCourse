# раздел 15.9 Встроенные функции any(), all(), zip(), enumerate(), задание 9
countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

for country, capital, populate in zip(countries, capitals, population):
    print(f'{capital} is the capital of {country}, population equal {populate} people.')
