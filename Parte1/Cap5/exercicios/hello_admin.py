search_user = str(input('What user you look for?: ')).strip()
users = ['admin', 'fabiano', 'jullyana', 'inacio']

try:
    if search_user in users:
        for user in users:
            if search_user == user:
                print(f'\nHello ' + str(search_user).title() +
                      ' you need see relatory of status!\n')
                break
            else:
                print(f'\nHello ' + str(search_user).title() + ', you logged!\n')
                break

    else:
        print(f'\n' + str(search_user).title() + ' is not registreded\n')
except Exception as error:
    print('%s' % (error))
