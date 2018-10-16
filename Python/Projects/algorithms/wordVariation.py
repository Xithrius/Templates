'''
if P(a, b, c, ...) = all the permutations,
then P(a, b, c, d ....) = {a + P(b, c, d, ...), b + P(a, c, d, ...) ,...}
'''

import time


def main():
    In = writeLine('input:')
    outList = []
    for i in range(len(In)):
        outList.append(In[i])
        print(outList)


# word = ''.join(str(e) for e in word


def writeLine(string, option='endWinput', t=0.0005):
    if option == 'endWinput':
        for i in string:
            print(i, end='', flush=True)
            time.sleep(t)
        In = input(' ')
        return In
    elif option == 'endWOinput':
        for i in string:
            print(i, end='', flush=True)
            time.sleep(t)
        print(end='\n')


main()
