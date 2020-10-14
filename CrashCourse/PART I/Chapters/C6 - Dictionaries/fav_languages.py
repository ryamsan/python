fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

language = fav_languages['sarah'].title()
print(f'Sarah\'s favourite language is {language}.')


print('''
--------------
''')

for name, language in fav_languages.items():
    print(f'{name.title()}\'s favourite language is {language.title()}!')

print('''
-------------- List in dictionary!
''')

fav_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in fav_languages.items():
    print(f'\n{name.title()}\'s favourite languages are:')

    for language in languages:
        print(f'\t{language.title()}')