def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user = build_profile('ryann', 'goh', location='singapore', education_lvl='junior college', age=19)

print(user)
