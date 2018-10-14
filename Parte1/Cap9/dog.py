class Dog():
    """Uma tentativa simple de modelar um cachorro."""

    def __init__(self, name, age):
        """Inicializa os atributos name e age."""
        self.name = name
        self.age = age

    def sit(self):
        """Simula um cachorro sentando em resposta a um comando."""
        print(self.name.title() + " in now sitting.")

    def roll_over(self):
        """Simula um cachorro rolando em resposta a um comando."""
        print(self.name.title() + " rolled over!. ")


"""My dog"""
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()


"""Your dog"""
your_dog = Dog('Kiara', 1)
print(f'Meu cachorro(a) chama ' + your_dog.name.title() + '.')
print(f'Ele(a) tem ' + str(your_dog.age) + ' de idade.')
your_dog.sit()
your_dog.roll_over()
