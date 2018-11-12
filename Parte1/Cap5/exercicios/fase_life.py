age = int(input('What your age?: '))


if age <= 2:
    print('Is a baby!')
elif age <= 4:
    print('You are a children!')
elif age <= 13:
    print('You are a kid!')
elif age <= 20:
    print('You are a teenager!')
elif age <= 65:
    print('You are a adult!')
else:
    print('You are a old!')
