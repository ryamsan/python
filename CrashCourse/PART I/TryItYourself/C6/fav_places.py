fav_places = {
    'bonnie': ['france', 'canada'],
    'andy': ['singapore', 'korea', 'france'],
    'toby': ['germany']
}

for name, places in fav_places.items():
    print(f'{name.title()}\'s favourite place(s) are:')
    for place in places:
        print(f'\t{place.title()}')