prompt = "\nEnter the name of a city you have visited:"
prompt += "\n(Enter 'quit' to end the programme.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f'I\'d love to go to {city.title()} one day!')