# Use of **kwargs, meaning you may not know what info will be passed in future
# **kwargs builds an empty dictionary eg **user_info to store as many key-values pairs as you want


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)
