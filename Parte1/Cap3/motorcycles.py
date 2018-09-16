# lista de motos
motorcycles = ['honda','yamaha','suzuki']

# mostra a lista de motos
#print(motorcycles)

# substitui a moto hoda pela moto ducati, alterando a listagem
#motorcycles[0] = 'ducati'

# mostra a lista de motos com a moto ducati
#print(motorcycles)

# adiciona a moto ducati a lista de motos
#motorcycles.append('ducati')

# mostra a lista de motos com a moto ducati inclusa
#print(motorcycles)

# inseri a moto ducati no começo da lista
motorcycles.insert(0, 'ducati')

# mostra a lista de motos
#print(motorcycles)

# remove um item da lista
#del motorcycles[3]

# mostra a lista de motos sem o item removido
#print(motorcycles)

# método pop() remove o último item da lista
# coloca o último item da lista na variável popped_motorcycles
popped_motorcycles = motorcycles.pop()

# mostra a lista de motos sem o último item a moto suzuki
print(motorcycles)

# mostra o item removido da lista, no caso a moto suzuki
print(popped_motorcycles)


# métodos de remoção de um item da lista
# del motorcycles['posição']
# motorcycles.pop('posição')
# motorcycles.remove('item') # no caso o texto que representa aquele item