class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'O Restaurande ' + self.restaurant_name.title() +
              ' de cozinha ' + self.cuisine_type + '.')

    def open_restaurant(self):
        print(f'Hoje ele(a) está aberto!')

    def read_number_served(self):
        print(f'O restaurante atendeu ' + str(self.number_served) + ' hoje!.')

    def set_number_served(self, client_served):
        self.number_served = client_served

    def increment_number_served(self, new_client_served):
        self.number_served += new_client_served


restaurant = Restaurant('MeuRestaurante', 'Comida')
restaurant.read_number_served()

restaurant.number_served = 23
restaurant.read_number_served()

restaurant.set_number_served(50)
restaurant.read_number_served()

restaurant.increment_number_served(100)
restaurant.read_number_served()