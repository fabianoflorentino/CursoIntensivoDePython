class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f'\nNome: ' + str(self.first_name))
        print(f'Último Nome: ' + str(self.last_name))

    def greet_user(self):
        print(f'\nSeja bem-vindo ' + str(self.first_name) +
              ' ' + str(self.last_name) + '\n')

    def read_login_attempts(self):
        print(f'Tentativas de Login: ' + str(self.login_attempts))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts -= 1

        if self.login_attempts == 0:
            print(f'Tentativas de login zeradas! ' +
                  str(self.login_attempts) + '.')


user_login = User('Fabiano', 'Florentino')
user_login.describe_user()
user_login.greet_user()
user_login.increment_login_attempts()
user_login.increment_login_attempts()
user_login.increment_login_attempts()
user_login.increment_login_attempts()
user_login.increment_login_attempts()
user_login.read_login_attempts()

print('-=' * 25)

user_login.reset_login_attempts()
user_login.reset_login_attempts()
user_login.reset_login_attempts()
user_login.reset_login_attempts()
user_login.reset_login_attempts()
