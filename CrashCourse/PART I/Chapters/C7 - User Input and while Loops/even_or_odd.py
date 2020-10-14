number = input("Enter a number, and I'll tell you if it's even or odd: ")

number = int(number)

if number % 2 == 0:
    print(f'The number, {number} is even.')

if number % 2 == 1:
    print(f'The number, {number} is odd.')
