import time


def main():
    In = writeLine('input:')
    for i in range(5):
        for x in range(len(In)):
            In = In[-1] + In[:-1]
            print(f'██ {In} ██ Variation {x}', end='\r')
            time.sleep(0.5)


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
