def greet_users(names):
    """Print a simple msg to each user in the list!"""

    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['hannah', 'jonas', 'tyrone']
greet_users(usernames)
