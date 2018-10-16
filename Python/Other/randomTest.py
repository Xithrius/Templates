# something here
# see what things do what

import time

x = input('something here: ')
print(x)
x = list(x)

for i in range(len(x) - 1):
    if x[i] != x[i + 1]:
        x[i], x[i + 1] = x[i + 1], x[i]

y = ''.join(str(e) for e in x)
print(y)
