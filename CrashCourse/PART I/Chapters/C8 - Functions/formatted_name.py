def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Optional formatted arg


def get_formatted_names2(first_name, last_name, middle_name=''):

    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()


musician = get_formatted_names2('jimi', 'hendrix')
print(musician)
musician = get_formatted_names2('john', 'hooker', 'lee')
print(musician)
