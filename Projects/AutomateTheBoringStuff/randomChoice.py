import random

pets = ['dog', 'cat', 'squid', 'spider', 'hamster', 'human', 'zombie']

for i in range(2):
    print(random.choice(pets))


pets = ['dog', 'cat', 'squid', 'spider', 'hamster', 'human']

random.shuffle(pets)

print(pets)