x = list('$updateStatus Help')
print(x[14:18])
x[0:14] = ''
print(x[0:4])
if ''.join(str(y) for y in x[0:4]) == 'Help':
    print(True)
