class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f'\nNome: ' + str(self.first_name))
        print(f'Último Nome: ' + str(self.last_name))
    
    def greet_user(self):
        print(f'\nSeja bem-vindo ' + str(self.first_name) + ' ' + str(self.last_name) + '\n')

"""User 1"""
user_1 = User('Fabiano','Florentino')
user_1.describe_user()
user_1.greet_user()

"""User 2"""
user_2 = User('Jullyana','Ferreira')
user_2.describe_user()
user_2.greet_user()

"""User 3"""
user_3 = User('Inácio','Gouveia')
user_3.describe_user()
user_3.greet_user()