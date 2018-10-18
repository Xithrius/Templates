import time


def writeLine(string, option='endWinput', t=0.01):
	if option == 'endWinput':
		for i in string:
			print(i, end='', flush=True)
			time.sleep(t)
		In = input(' ')
		return In

	elif option == 'endWinputLibrary':
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


# Used for writeline
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


def loadBar(interval):
	if interval == 'random':
		pass

	elif interval == 'corrupted':
		pass

	elif interval == 'intervaled':
		z = 0
		for i in range(101):
			if i % 10 == 0 or i == 0:
				y = ' ' * (10 - z)
				x = ':' * z
				z += 1
			print(f'| {x}{y} | {i}%', end='\r', flush=True)
			time.sleep(0.1)
	else:
		raise ValueError


def rotating(string, length):
	if length == 'infinite':
		for i in range(5):
			for x in range(len(In)):
				In = In[-1] + In[:-1]
				print(f'██ {In} ██ Variation {x}', end='\r')
				time.sleep(0.5)
	elif length.isnumeric():
		length = int(length)
		for i in range(length):
			for x in range(len(In)):
				In = In[-1] + In[:-1]
				print(f'██ {In} ██ Variation {x}', end='\r')
				time.sleep(0.5)


def Corrupted(string, interval):
	pass
