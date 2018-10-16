'''
Countdown to a date
'''

import datetime as dt
import time

message = input('Message? ')
y = int(input('Year? '))
m = int(input('Month? '))
d = int(input('Day? '))


date = dt.datetime(y, m, d)

while dt.datetime.now() < date:
    x = date - dt.datetime.today()
    print(x, end='\r')

print(message)
time.sleep(5)
quit()
