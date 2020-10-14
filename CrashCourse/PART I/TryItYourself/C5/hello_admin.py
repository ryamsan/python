users = ['dddd', 'aaaa', 'xxxx', 'admin', 'bbbb']

for user in users:
    if user == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {user}, thank you for logging in again.')



# users = ['dddd', 'aaaa', 'xxxx', 'admin', 'bbbb']
#
# for i in range(len(users)):
#     users.pop()
# print(users)
#
# if users == []:
#     print('We need to find some users')

users = []

if users:
    for user in users:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {user}, thank you for logging in again.')

else:
    print('We need to find some users!')