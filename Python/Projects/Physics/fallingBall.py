'''
The ball is falling
'''


def Acceleration(t):

    d = 4.9 * (t ** 2)
    return d


tString = input('Time of fall: ')
t = float(tString)
d = Acceleration(t)
print('fallen', d, 'units')
