import json

glossary = {
    'tupla': 'Uma lista com itens que não pode ser modificada.',
    'variavel': 'Espaço de memória que guarda uma valor.',
    'lista': 'Conjunto de valores armazenados em uma lista.',
    'dicionario': 'Conjunto de valores chave valor associados.',
    'tipos de dados': 'string(str), integer(int), float(float), são tipos de dados.'
}

glossary['pep8'] = 'Guia de estilo da linguagem, ajuda a deixar o código mais pythonico!.'
glossary['indice'] = 'Posição decada item em um lista.'
glossary['append'] = 'Método para adicionar um valor a uma lista.'
glossary['linguagens'] = 'Python, C e Ruby são linguagens de programação muito poderosas.'
glossary['import this'] = 'Zen do Python.'

for key, value in glossary.items():
    print(f'\n{key}: {value}')
