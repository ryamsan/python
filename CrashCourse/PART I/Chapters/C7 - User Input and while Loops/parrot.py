# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)


# prompt = "\nTell me something and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the programme. "
# message = ""
#
# while message != 'quit':
#     message = input(prompt)
#
#     if message != 'quit':  # To fix the programme printing quit as if it is being repeated back to you.
#         print(message)

'''
Using a flag
'''

prompt = "\nTell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the programme. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
