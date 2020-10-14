# prompt = "\nTell me what topping you would like on your pizza:"
# prompt += "\nEnter 'quit' to end the programme. "
#
# while True:
#     topping = input(prompt)
#     if topping == 'quit':
#         break
#     else:
#         print(f"I will add {topping} to your pizza.")



prompt = "\nTell me what topping you would like on your pizza:"
prompt += "\nEnter 'quit' to end the programme. "

topping = ""

while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print(f"I will add {topping} to you pizza")


