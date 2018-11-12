request_toppings = []

if request_toppings:
    for request_topping in request_toppings:
        print('Adding ' + request_topping + '.')
    print(f'\nFinished making your pizza!\n')
else:
    print(f'\nAre you sure you want a plain pizza?\n')
