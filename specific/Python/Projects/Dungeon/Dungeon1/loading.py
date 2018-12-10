# Loading bars

import time
import random

def loading(string, x):

    if x == 0:
        print('x != 0 w/ string')
        print(ValueError)

    # █
    if x == 1:

        if string == 'true':
            for i in range(100):
                print('█', sep='', end='', flush=True)
                time.sleep(0.001)
            print(end='\n')
            return True


    # | / - \\
    if x == 2:

        if string == 'true':
            for i in range(random.randint(5, 10)):
                for c in '|/-\\':
                    print(c, sep='', end='\r', flush=True)
                    time.sleep(0.25)
            return True

    if x == 3:

        if string == 'true':

            for i in range(100):
                print('█', sep='', end='', flush=True)
                time.sleep(0.1)
            return True
