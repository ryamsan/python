prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' to end the programme. "

while True:
    age = input(prompt)

    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        print("You get in for free!")

    elif age < 12:
        print(f"You get in for $10.")

    else:
        print(f"You get in for $15.")