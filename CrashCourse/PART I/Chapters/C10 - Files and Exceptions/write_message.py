filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('I love programming.\n')  # Creates a new text file from scratch.
    file_object.write('I love creating new games.\n')


with open(filename, 'a') as file_object:  # Append mode! Add stuff that hasn't been added yet!
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")