alien_0 = {}

alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'

print(f'\nOriginal x-position: ' + str(alien_0['x_position']))

# Move o alienigina para a direita
# Determina a distância que o alienigina deve se deslocar de acordo com sua
# velocidade atual
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Este deve ser um alienigia rápido
    x_increment = 3

# A nova posição é a posição antiga somada ao incremento
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f'\nNew x-position: ' + str(alien_0['x_position']) + '\n')