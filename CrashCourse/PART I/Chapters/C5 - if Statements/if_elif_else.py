# age = 12
#
# if age < 4:
#     print('The admission fee is $0.')
# elif age < 18:
#     print('The admission fee is $25.')
# else:
#     print('The admission fee is $40.')


age = 25

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f'Your admission fee is ${price}.')
