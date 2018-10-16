# lines

import time

w0 = 0
while w0 < 100:
    w0 = w0 + 1
    print('loading...', w0, '%', sep='', end='\r', flush=True)
    time.sleep(0.1)
