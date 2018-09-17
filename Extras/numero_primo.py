primo = 0

while True and primo != 2:
    primo = 0
    try:
        number = int(input(f'\nDigite um número inteiro: '))

        for numbers in range(1, number + 1):
            result = (number % numbers)

            if result == 0:
                primo += 1

        if primo == 2:
            print(f'\nÉ um numero primo!\n')
            break
        else:
            print(f'\nNão é um numero primo...')

    except ValueError:
        print(f'\nNão é uma entrada válida!...\n')
    except KeyboardInterrupt:
        print(f'\nSaindo ...\n')
        break
