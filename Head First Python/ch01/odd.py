from datetime import datetime
import time
import random

print('Start program')
#odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
#        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
#        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
# list comprehension
odds = [n for n in range(1, 60, 2)]
print(odds)
for i in range(5):
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print(f'Minutes {right_this_minute: 2d} is odd')
    else:
        print(f'Minutes {right_this_minute: 2d} is even')
    rnd = random.randint(1, 20)
    print(f'Sleep for {rnd: 2d} seconds')
    time.sleep(rnd)
print('The end')
