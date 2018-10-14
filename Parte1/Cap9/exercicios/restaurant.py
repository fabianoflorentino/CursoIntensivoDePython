class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'O Restaurande ' + self.restaurant_name.title() +
              ' de cozinha ' + self.cuisine_type + '.')

    def open_restaurant(self):
        print(f'Hoje ele(a) está aberto!')


"""Restaurante 1"""
restaurant_1 = Restaurant('ragazzo', 'italiana')
restaurant_1.describe_restaurant()
print(f'\nMeu restaurante preferido de comida ' + str(restaurant_1.cuisine_type) +
      ' é o ' + str(restaurant_1.restaurant_name.title()) + '.\n')
restaurant_1.open_restaurant()
print('')

"""Restaurante 2"""
restaurant_2 = Restaurant('PizzaHut', 'pizza')
restaurant_2.describe_restaurant()
print(f'\nA melhor ' + str(restaurant_2.cuisine_type) +
      ' é da ' + str(restaurant_2.restaurant_name.title()) + '.\n')
restaurant_2.open_restaurant()
print('')

"""Restaurante 3"""
restaurant_3 = Restaurant("McDonald's", 'hamburger')
restaurant_3.describe_restaurant()
print(f'\nSou da geração que acha que ' + str(restaurant_3.cuisine_type) +
      ' tem que ser ' + str(restaurant_3.restaurant_name.title()) + '.\n')
