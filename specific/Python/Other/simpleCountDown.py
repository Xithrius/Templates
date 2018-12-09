'''
countdown timer
'''

import time


def countdown(t):

    s = input('time interval: ')
    if s < 0:
        print(ValueError)
    else:
        pass

    t = input('time: ')
    if t < 0:
        print(ValueError)
    else:
        pass

    m = input('message: ')
    if m == int():
        print('no numbers allowed')
    else:
        pass

    while t > 0:
        print(t)
        time.sleep(s)
        t = t - 1
    print(m)


'''
Freq = 1000 # Set Frequency To 2500 Hertz
Dur = 500 # Set Duration To 1000 ms == 1 second
import winsound
if n == 0:
    Freq = 1000
    Dur = 500
    winsound.Beep(Freq, Dur)
    print('done!')
'''
