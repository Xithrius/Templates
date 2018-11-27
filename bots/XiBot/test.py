x = list(input(': '))
x[0:14] = ''
print(''.join(str(i) for i in x))
for i in range(len(x)):
    if x[i] == ',':
        if x[i + 1] == ' ':
            status = x[0:i]
            desc = x[i + 2:]
status = ''.join(str(y) for y in status)
desc = ''.join(str(y) for y in desc)
print(status)
print(desc)
