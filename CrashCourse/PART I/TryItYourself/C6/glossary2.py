glossary = {
    'string': 'A series of characters',
    'comment': 'A note that the Python interpreter ignores',
    'list': 'A collection of items in a particular order and can be amended',
    'loop': 'Work through a collection of items, one at a time',
    'dictionary': 'A collection of key-value pairs'
}

for word in glossary.keys():
    print(f'{word.title()}: {glossary[word]}')

    
