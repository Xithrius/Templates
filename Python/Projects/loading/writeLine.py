import time

def main_WriteLine(string, option='endWinput', t=0.01):
    if option == 'endWinput':
        for i in string:
            print(i, end='', flush=True)
            time.sleep(t)
        In = input(' ')
        checkOut = inputLibrary(string, In)
        if checkOut != False:
            return checkOut
        else:
            main_WriteLine(string)
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
