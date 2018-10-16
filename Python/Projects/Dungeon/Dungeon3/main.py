import os
import json
import time


def instructions():
    # writeLine('', 'endWOinput')
    writeLine('+-INSTRUCTIONS', 'endWOinput')
    writeLine('', 'endWOinput')


def pathing(option):
    if option == 'dirPath':
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return dir_path


def writeLine(string, option='endWinput', t=0.01):
    if option == 'endWinput':
        for i in string:
            print(i, end='', flush=True)
            time.sleep(t)
        In = input(' ')
        checkOut = inputLibrary(string, In)
        if checkOut != False:
            return checkOut
        else:
            writeLine(string)
    elif option == 'endWOinput':
        for i in string:
            print(i, end='', flush=True)
            time.sleep(t)
        print(end='\n')


def inputLibrary(string, In):
    check = True
    while check:
        for i in range(len(string)):
            if string[i] == '[':
                bracketForward = i
            elif string[i] == ']':
                bracketBackward = i
                check = False
    newString = string[bracketForward:bracketBackward]
    optionList = []
    for i in newString:
        if i.isalpha():
            optionList.append(i.lower())
    if In in optionList:
        return In
    elif In not in optionList:
        return False


def load(option, interval, intervalTime):
    if option == 'spinner':
        for i in range(interval):
            for i in '|/-\\':
                print(i, end='\r', flush=True)
                time.sleep(intervalTime)
    elif option == 'loadBar':
        pass
    else:
        raise ValueError()


def backup(string):
    if string == 'reset':
        characterInfo = {'position': (0, 0), 'life': 100, 'exp': (0, 0)}
        with open(pathing('dirPath') + '/saveGame.json', 'w') as f:
            json.dump(characterInfo, f)
        return characterInfo
    elif string == 'load':
        if os.path.isfile(pathing('dirPath') + '/saveGame.json') is False:
            backup('reset')
        else:
            with open(pathing('dirPath') + '/saveGame.json', 'r') as f:
                characterInfo = json.load(f)
            return characterInfo
    elif string == 'save':
        characterInfo = {'position': Chracter.position,
                         'life': Character.life,
                         'exp': Character.exp}


def main():
    In = writeLine('Instructions? [Y/N]:')
    if In == 'y':
        instructions()
    else:
        pass

    In = writeLine('Restart or load from save? [R/L/Q]:')
    if In == 'r':
        objects = backup('restart')
        return objects
    elif In == 'l':
        objects = backup('load')
        return objects
    elif In == 'q':
        quit()


class Environment:

    def __init__(self):
        pass



class Character:
    objects = main()

    health = objects['health']
    position = objects['position']
    exp = objects['exp']
    writeLine(f'Health: {Character.health}, Position" {Character.position}, exp: {Character.exp}', 'endWOinput', 0.001)

    def __init__(self):
        pass



Character()
