filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

print(type(lines))

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


''' sdsdsd '''


filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:52]}...")
print(len(pi_string))


''' birthday contained in Pi? '''


filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday (DDMMYY): ")
if birthday in pi_string:
    print("Your birthday appears in the first millions digits of pi!")
else:
    print("Your birthday does not appear in the first millions digits of pi!")