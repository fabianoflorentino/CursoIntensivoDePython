import json

glossary = dict()

glossary['word1'] = str(input(f'\nDigite uma palavra: '))
glossary['means1'] = str(input(f'Digite seu significado: '))

glossary['word2'] = str(input(f'\nDigite uma palavra: '))
glossary['means2'] = str(input(f'Digite seu significado: '))

glossary['word3'] = str(input(f'\nDigite uma palavra: '))
glossary['means3'] = str(input(f'Digite seu significado: '))

glossary['word4'] = str(input(f'\nDigite uma palavra: '))
glossary['means4'] = str(input(f'Digite seu significado: '))

glossary['word5'] = str(input(f'\nDigite uma palavra: '))
glossary['means5'] = str(input(f'Digite seu significado: '))

# print(f'\n ' + glossary['word1'] + ': ' + glossary['means1'] )
# print(f'\n ' + glossary['word2'] + ': ' + glossary['means2'] )
# print(f'\n ' + glossary['word3'] + ': ' + glossary['means3'] )
# print(f'\n ' + glossary['word4'] + ': ' + glossary['means4'] )
# print(f'\n ' + glossary['word5'] + ': ' + glossary['means5'] )

print(json.dumps(glossary, indent=4))