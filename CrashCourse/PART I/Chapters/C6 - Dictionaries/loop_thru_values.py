fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print('The following languages have been mentioned:')

for language in fav_languages.values():
    print(language.title())

print('''
This doesn't check for repeats...
''')

fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print('The following languages have been mentioned:')

for language in set(fav_languages.values()):
    print(language.title())
