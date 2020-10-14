fav_numbers = {
    'ssss': [16, 13],
    'dddd': [12],
    'ffff': [2, 7, 9],
    'jjjj': [7, 10, 32],
    'pppp': [10, 2, 5]
}

for name, numbers in fav_numbers.items():
    print(f"{name} likes the numbers:")
    for number in numbers:
        print(f"\t- {number}")