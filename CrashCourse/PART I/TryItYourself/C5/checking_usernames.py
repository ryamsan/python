current_users = ['dddd', 'aaaa', 'xxxx', 'admin', 'bbbb']

new_users = ['llll', 'wwww', 'ssss', 'Admin', 'bBbb']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print('You need enter a new username as the username has been taken!')
    else:
        print('Username is available!')


