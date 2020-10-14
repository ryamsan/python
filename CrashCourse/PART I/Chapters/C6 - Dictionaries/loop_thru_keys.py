fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name in fav_languages.keys():
    print(name.title())

print('''
--------------
''')

fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

friends = ['phil', 'sarah']

for name in fav_languages: # This works too instead of fav_languages.keys(); Python assumes this
    print(f'Hi {name.title()}.')

    if name in friends:
        language = fav_languages[name].title()
        print(f'\t{name.title()}, I see you love {language}!')

print('''
--------------
''')


fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

if 'erin' not in fav_languages.keys():
    print('Erin, please take our poll!')