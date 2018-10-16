import time
import json
import os


# fancy printing
def writeLine(string, option='endWinput', t=0.01):

    # Priting every single character next to eachother at interval t
    # After the print is done, a input will be displayed on the same line
    if option == 'endWinput':
        for i in string:
            if i != '.' or '?' or ',':
                print(i, end='', flush=True)
                time.sleep(t)
            else:
                print(i, end='', flush=True)
                time.sleep(t * 50)

        In = input(' ')
        return In

    # Same as above, but input will not be displayed when the print is finished
    if option == 'endWOinput':
        for i in string:
            print(i, end='', flush=True)
            time.sleep(t)
        print(end='\n')


# Inputting a different option will give you a different path
def pathing(option):

    if option == 'dirPath':
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return dir_path

    if option == 'cookiePath':
        dir_path = os.path.dirname(os.path.realpath(__file__))
        cookiePath = dir_path + '/cookies.txt'
        return cookiePath

    elif option == 'buildingPath':
        dir_path = os.path.dirname(os.path.realpath(__file__))
        buildingPath = dir_path + '/buildings.txt'
        return buildingPath


# getting or resetting information
def main():

    check = True
    In = writeLine('Restart or load from save? [R/L]:')

    # Restarting
    if 'restart'.startswith(In.lower()) or 'RESTART'.startswith(In.upper()):
        objects = {'cookies': 1, 'buildings': [(1), (0), (0), (0), (0), (0)]}

        # Using json to restart the save file
        with open('saveGame.json', 'w') as f:
            json.dump(objects, f)
        return objects

    # Using json to load the save information from a .json file
    elif 'load'.startswith(In.lower()) or 'LOAD'.startswith(In.upper()):

        with open('saveGame.json', 'r') as f:
            objects = json.load(f)
            return objects

    else:
        check = True
        writeLine('Restart or Load', 'endWOinput')


class Objects:

    # Starting main and then getting the save file from it
    objects = main()

    # Searching for 'cookies' in the dictionary, then returning the value
    cookies = objects['cookies']
    # Searching for 'buildings' in the dictionary, then returning the set of values
    buildings = objects['buildings']

    def __init__(self):
        check = True
        writeLine(
            'buy/wait/instructions/quit is shown as [B/W/I/Q]', 'endWOinput')

        while check:
            option = writeLine('[B/W/I/Q]:')

            # Setting boolean options
            buy = 'buy'.startswith(
                option.lower()) or 'BUY'.startswith(option.upper())
            wait = 'wait'.startswith(
                option.lower()) or 'WAIT'.startswith(option.upper())
            instructions = 'instructions'.startswith(
                option.lower()) or 'INSTRUCTIONS'.startswith(option.upper())
            quit = 'quit'.startswith(
                option.lower()) or 'QUIT'.startswith(option.upper())

            if buy:
                getObject()

            if wait:
                waitTimer()

            if instructions:
                instruc()

            if quit:
                check = False
                saveQuit()

            elif not buy or wait or quit:
                check = True
                writeLine(
                    'buy/wait/instructions/quit is shown as [B/W/I/Q]', 'endWOinput')


def getObject():

    check = True

    while check:
        basePrice = [10, 1000, 10000, 100000, 1000000, 10000000]
        for i in range(0, 6):
            price = basePrice[i] + ((Objects.buildings[i] + 1))
            writeLine(f'Type {i} price: {price}', 'endWOinput')

        buildingType = writeLine('Type [0/1/2/3/4/5/Q]:')

        if buildingType.isnumeric():
            buildingType = int(buildingType)
            In = writeLine(
                f'You have selected option {buildingType}. How many would you like to purchase? [AMOUNT/QUIT]:')

            if In.isnumeric():
                check = False
                In = int(In)
                basePrice = [10, 1000, 10000, 100000, 1000000, 10000000]
                price = basePrice[buildingType] + \
                    ((Objects.buildings[buildingType] + 1) * In)

                if price > Objects.cookies:
                    writeLine(
                        f'You do not have enough cookies to purchase this. The price is {price}. You only have {Objects.cookies}, so you need {price - Objects.cookies} more cookies.', 'endWOinput')
                    check = False

                elif price <= Objects.cookies:
                    yn = writeLine(f'The price is {price}. Confirm? [Y/N]:')

                    if 'yes'.startswith(yn.lower()) or 'YES'.startswith(yn.upper()):
                        Objects.cookies -= price
                        Objects.buildings[buildingType] += In

                        check0 = True
                        while check0:
                            In = writeLine('Check objects? [Y/N]:')

                            if 'yes'.startswith(In.lower()) or 'YES'.startswith(In.upper()):
                                check0 = False
                                writeLine(
                                    f'You now have {Objects.cookies} cookies', 'endWOinput')
                                writeLine('You also now have: ', 'endWOinput')
                                for i in range(0, 6):
                                    writeLine(
                                        f'Type {i}: {Objects.buildings[i]}', 'endWOinput')

                            elif 'no'.startswith(In.lower()) or 'NO'.startswith(In.upper()):
                                check = False

                            elif NoneType():
                                check = True
                                writeLine(
                                    'Either yes or no, which is shown as [Y/N]', 'endWOinput')

                            else:
                                check = True
                                writeLine(
                                    'Either yes or no, which is shown as [Y/N]', 'endWOinput')

                    elif 'no'.startswith(yn.lower()) or 'NO'.startswith(yn.upper()):
                        pass

            elif 'redo'.startswith(In.lower()) or 'REDO'.startswith(In.upper()):
                check = True

        elif 'quit'.startswith(buildingType.lower()) or 'QUIT'.startswith(buildingType.upper()):
            check = False

        elif buildingType != int():
            writeLine('Enter type between 0 and 5', 'endWOinput')
            check = True


def waitTimer():

    check = True

    while check:
        t = writeLine('How long should the timer run?')

        # if the number can be converted into a string, then the statement returns True
        if t.isnumeric():
            check = False
            t = int(t)
            cps = 0

            # When starting the loop of cookies, cps gets all buildings' cps added together
            for i in range(0, 6):
                cps += (Objects.buildings[i] ** ((2 + i) / 2))

            # The loop that starts adding cps to cookies
            for i in range(t):
                Objects.cookies += cps
                print(
                    f'cps: {cps}, time left: {t - i}, Cookies: {Objects.cookies}', end='\r', flush=True)
                time.sleep(1)

            print(end='\n')

        else:
            check = True


def instruc():

    writeLine('/// BUYING OBJECTS ///', 'endWOinput', 0.001)
    writeLine('When you type buy, you will be brought to a catalog.',
              'endWOinput', 0.001)
    writeLine('If you do not have enough money to buy the object, the shop will tell you how much more you need.', 'endWOinput', 0.001)

    writeLine('/// WAITING FOR COOKIES ///', 'endWOinput', 0.001)
    writeLine('When you type wait, you will be asked how long you would like to wait.',
              'endWOinput', 0.001)
    writeLine('The time input is in seconds, so do not put in some weird format of time',
              'endWOinput', 0.001)

    writeLine('/// INSTRUCTIONS ///', 'endWOinput', 0.001)
    writeLine('When you type instructions, you will be brought here, and you can read it again.',
              'endWOinput', 0.001)

    writeLine('/// QUIT ///', 'endWOinput', 0.001)
    writeLine('When you quit, the progress will be saved automatically.',
              'endWOinput', 0.001)
    writeLine('The save file will be in the same folder as the main file.',
              'endWOinput', 0.001)


def saveQuit():

    # Gets the objects that had been modified throughout gameplay
    state = {'cookies': Objects.cookies, 'buildings': Objects.buildings}

    with open('saveGame.json', 'w') as f:
        json.dump(state, f)

    writeLine('Quitting...', 'endWOinput', 0.1)


# Starts class 'Objects' to run main, that runs many other functions
Objects()
