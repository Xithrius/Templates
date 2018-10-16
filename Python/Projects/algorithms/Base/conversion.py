'''
https://www.electronics-tutorials.ws/binary/bin_2.html

N is a real positive number
b is the diget
q is the base value
N = b(q^i)

binary     : q = 2
octal      : q = 8
decimal    : q = 10
hexidecimal: q = 16

Binary:
number =

'''

import json
import time
import os


def main():
    conversionType = writeLine('Convert binary, octal, decimal, or hexidecimal [B/O/D/H]:')
    if conversionType == 'b':
        q = 2
    elif conversionType == 'o':
        q = 8
    elif conversionType == 'd':
        q = 10
    elif conversionType == 'h':
        q = 16

    In = writeLine('Encode/Decode [E/D]:')
    if In == 'e':
        Error = True
        while Error:
            In = writeLine('input string of numbers:', 'endWfreeinput')
            errorList = []
            passList = []
            for i in range(len(In)):
                if In[i].isnumeric() is False:
                    errorList.append(In[i])
                elif In[i].isnumeric():
                    passList.append(In[i])
            if len(errorList) == 0:
                print('No errors, moving on')
                Error = False
                In = int(In)
                encode(q, In)
            else:
                errorList = ''.join(str(e) for e in errorList)
                passList = ''.join(str(e) for e in passList)
                writeLine(f'Errors in input: {errorList}', 'endWOinput')
                writeLine(f'Nonerrors in input: {passList}', 'endWOinput')
                Error = True

    elif In == 'd':
        Error = True
        while Error:
            In = writeLine('input 1s and 0s', 'endWfreeinput')
            errorList = []
            passList = []
            for i in range(len(In)):
                if In[i].isnumeric() is False:
                    errorList.append(In[i])
                elif In[i].isnumeric():
                    passList.append(In[i])
            if len(errorList) == 0:
                print('No errors, moving on')
                Error = False
                In = int(In)
                decode(q, In)
            else:
                errorList = ''.join(str(e) for e in errorList)
                passList = ''.join(str(e) for e in passList)
                writeLine(f'Errors in input: {errorList}', 'endWOinput')
                writeLine(f'Nonerrors in input: {passList}', 'endWOinput')
                Error = True


def encode(q, string):
    out = []
    #while True:
    #    if string != 0:
    remainder = string % q
    print(q)
    print(remainder)


def decode(q, string):
    pass


def writeLine(string, option='endWinput', t=0.005):
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
    elif option == 'endWfreeinput':
        for i in string:
            print(i, end='', flush=True)
            time.sleep(t)
        In = input(' ')
        return In


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


main()
