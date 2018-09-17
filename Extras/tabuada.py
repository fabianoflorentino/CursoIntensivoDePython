while True:
    try:
        num = int(input(f'\nQual tabuada você deseja: '))

        for tab in range(1, 11):
            result = (int(num) * int(tab))
            print(str(num) + ' x ' + str(tab) + ' = ' + str(result))
        break

    except ValueError:
        print(f"Oops!  não é um número válido.  tente novamente...")
    except KeyboardInterrupt:
        print(f'\nSaindo ...\n')
        break
