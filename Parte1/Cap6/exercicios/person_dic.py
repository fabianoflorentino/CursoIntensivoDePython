#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

person = {}

try:
    person['first_name'] = str(
        input(f'\nDigite seu primeiro nome: ')).strip().title()
    person['last_name'] = str(
        input('Digite seu último nome: ')).strip().title()
    person['age'] = str(input('Digite sua idade: ')).strip()
    person['city'] = str(input('Cidade onde nasceu: ')).strip().title()
except ValueError:
    print(f'\nAs informações solicitadas estão erradas, Por favor digite os dados novamente.')


print(json.dumps(person, indent=4))
