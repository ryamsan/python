rivers = {
    'nile': 'egypt',
    'yangtze': 'china',
    'ganges': 'india'
}

for river in rivers.keys():
    print(f'The {river.title()} River runs through {rivers[river].title()}')

print('''
--------------
''')

for river in rivers.keys():
    print(river.title())


for river in rivers.keys():
    print(rivers[river].title())