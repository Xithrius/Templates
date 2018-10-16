import time

'''
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
'''
number = 1
x = [1, 1]
i = 0
while True:
    x.insert((i + 1), (x[i - 1] + x[i]))
    print(f'█ Row {number} █ {x[i]}')
    i += 1
    number += 1
    # time.sleep(0.01)
