'''
# will be randomly generated and spoken
'''
import time
import random as r
t = 0
rNumber = r.randint(10000, 99999)
while t < 1000000:
    t = t + 1
    rWait = r.randint(0, 60)
    print('Number is', rNumber)
    time.sleep(rWait)
