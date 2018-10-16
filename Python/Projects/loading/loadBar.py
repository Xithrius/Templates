import time
import random

def main_loadbar(interval):
    
    if interval == 'random':
        pass
    
    elif interval == 'corrupted':
        pass
    
    elif interval == 'intervaled':
        z = 0
        for i in range(101):
            if i % 10 == 0 or i == 0:
                y = ' ' * (10 - z)
                x = ':' * z
                z += 1
            print(f'| {x}{y} | {i}%', end='\r', flush=True)
            time.sleep(0.1)
    else:
        print(ValueError)


main_loadbar('intervaled')
