from datetime import datetime
import random
import time
Odd = list(range(1,60,2))
print(Odd)
for i in range(5):
    right_this_minute = datetime.today().minute
    if right_this_minute in Odd:
        print('This minute seems a little odd.')
    else:
        print('Not an odd minute')
    wait_time = random.randint(1,10)
    time.sleep(wait_time)