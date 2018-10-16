# movement can cause death
# Dungeon V 1

import time
import random

import YesNo
import upDownLeftRight
import loading
import runDirection

def Enter():


    if YesNo.yesNo('Would you like to enter the dungeon?'):


        for i in range(101):
            print('Loading dungeonV01...', i, '%', sep='', end='\r', flush=True)
            time.sleep((random.randint(1, 7)) / 50)
        print('\n', end='')


        if loading.loading('true', 1):
            for i in 'Which direction would you like to go?':
                time.sleep(0.05)
                print(i, end='', flush=True)
            if upDownLeftRight.upDownLeftRight('') is 90: # up
                if runDirection.up() is False:
                    exit()

            if upDownLeftRight.upDownLeftRight('') is 270: # down
                if runDirection.down() is False:
                    pass

            if upDownLeftRight.upDownLeftRight('') is 180: # left
                if runDirection.left() is False:
                    pass

            if upDownLeftRight.upDownLeftRight('') is 0: # right
                if runDirection.right() is False:
                    pass


    else:
        for x in 'quitting...':
            time.sleep(0.1)
            print(x, sep='', end='', flush=True)
        time.sleep(1.2)


Enter()
