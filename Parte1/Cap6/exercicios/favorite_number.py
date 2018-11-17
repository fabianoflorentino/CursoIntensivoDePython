import json


favorite_number = dict()

favorite_number['name1'] = str(input(f'\nDigite seu nome: '))
favorite_number['number1'] = str(input(f'Digite seu número favorito: '))
favorite_number['name2'] = str(input(f'\nDigite seu nome: '))
favorite_number['number2'] = str(input(f'Digite seu número favorito: '))
favorite_number['name3'] = str(input(f'\nDigite seu nome: '))
favorite_number['number3'] = str(input(f'Digite seu número favorito: '))


print(json.dumps(favorite_number, indent=4))