favorite_languages = {
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'Ruby',
    'phil': 'Python'
}

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(f" Hi " + name.title() + ", I see your favorite language is " +
              favorite_languages[name].title() + "!.")
