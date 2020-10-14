
# 100 flips! How many streaks of 6!


import random

total_streaks = 0
current_streak = 0

flip = []
for i in range(100):
    flip.append(random.choice(['H', 'T']))

print(flip)

for i in range(len(flip)):
    if i == 0:
        current_streak += 1
    else:
        if flip[i] == flip[i-1]:
            current_streak += 1
        else:
            current_streak = 1
    # print(current_streak)

    if current_streak == 6:
        total_streaks += 1

print(total_streaks)
