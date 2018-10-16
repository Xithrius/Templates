# Dungeon main V2

import random
import time


def init():
    user = input('name: ')
    loadLine('welcome, ' + user, 'n')
    loader(0)
    loadLine('Enter the dungeon?', 'n')
    in1 = input('[Y/N]: ')
    if 'yes'.startswith(in1.lower()):
        loader(1)
        if main() is False:
            reset()
    if 'no'.startswith(in1.lower()):
        exit(0)
    else:
        return ValueError
        reset(0)


def loadLine(string, option, x=0.075):
    if option == 'n':
        for i in string:
            print(i, end='', flush=True)
            time.sleep(x)
        print(end='\n')
    if option == 'r':
        for i in string:
            print(i, end='', flush=True)
            time.sleep(x)
        print(end='\r')


def loader(x):
    if x == 0:
        for i in range(100):
            print('█', sep='', end='', flush=True)
            time.sleep(random.randint(1, 10) / 300)
        print(end='\n')

    if x == 1:
        pass


def exit(x):
    if x == 0:
        loadLine('██.█...█.███.███.███.██...█.██............', 'n', 0.005)
        loadLine('█...█.█...█...█...█..██...█.█.............', 'n', 0.005)
        loadLine('██...█....█...█...█..█..█.█.█.███.........', 'n', 0.005)
        loadLine('█...█.█...█...█...█..█...██.█..█..........', 'n', 0.005)
        for i in range(3):
            loadLine('██.█...█.███..█..███.█...██.████...█......', 'r', 0.005)
            loadLine('██.█...█.███..█..███.█...██.████...█..█...', 'r', 0.005)
            loadLine('██.█...█.███..█..███.█...██.████...█..█..█', 'r', 0.005)
        print(end='\n')
    if x == 1:
        line = 'quitting...████████'
        line = list(line)
        for x in range(random.randint(1, 5)):
            for i in range(len(line)):
                pass


def main():
    loadLine('Entering...', 'n', 0.075)
    loadLine('Starting difficulty', 'n')
    setDiff = input('[0/1/2/3/4/5]: ')
    if '0'.startswith(setDiff.lower()):
        pass
    if '1'.startswith(setDiff.lower()):
        pass
    if '2'.startswith(setDiff.lower()):
        pass
    if '3'.startswith(setDiff.lower()):
        pass
    if '4'.startswith(setDiff.lower()):
        pass
    if '5'.startswith(setDiff.lower()):
        pass
    else:
        return ValueError


def life():
    pass


def reset(string):
    if string == 0:
        init()
    if string == 1:
        loadLine('restart? ', 'n')
        reset = input('[Y/N]: ')
        if 'yes'.startswith(reset.lower()):
            pass
        if 'no'.startswith(reset.lower()):
            pass


def Error():
    if main() is ValueError:
        print(ValueError)
        quit()
    if lines() is ValueError:
        print(ValueError)
        quit()
    if reset() is ValueError:
        print(ValueError)
        quit()

def lines(x):

    #diff level 1
    d1 = {1: '',
          2: ''}


init()
