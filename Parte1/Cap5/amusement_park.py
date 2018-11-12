age = input('What your age?: ')

if int(age) < 4:
    print('Your admission cost is $0.')
elif int(age) < 18:
    print('Your admission cost is $5.')
else:
    print('Your admission cost is $10.')
