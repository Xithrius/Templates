import loader

import pyautogui
import time
import json
import os
import distutils.dir_util

pyautogui.FAILSAFE = True
#x = pyautogui.confirm('A save file exists. Delete and reset?')

def main():
	In = loader.writeLine('Enter your name:')
	In1 = loader.writeLine(f'Greetings {In}. Create new save? [Y/N]:')
	if In1 == 'n':
		password = loader.writeLine('Enter password:')
	if In1 == 'y':
		loader.writeLine('Creating new save...', 'EndWOinput')
		generateFiles()
		generateFileProperties()
		saveDecision()


def generateFiles():
	try:
		distutils.dir_util.mkpath(pathing('SaveGames'))
		return False
	except FileExistsError:
		pass


def saveDecision():
	saveFile = False
	i = 0
	while False:
		try:
			with open(pathing('SaveGames') + f'/save{i}.json', 'w+') as f:
				x = {"Name": 0, "Pass": 0, "Cookies": 0, "Buildings": 0}
				json.dump(x, f)
				SaveFile = True
		except FileExistsError:
			i += 1



def generateFileProperties():
	loader.writeLine('cookieMaker2.py properties:', 'endWOinput', 0.1)
	loader.writeLine(f'File ----------> : {__file__}', 'endWOinput')
	loader.writeLine(f'Access time ---> : {time.ctime(os.path.getatime(__file__))}', 'endWOinput')
	loader.writeLine(f'Modified time -> : {time.ctime(os.path.getmtime(__file__))}', 'endWOinput')
	loader.writeLine(f'Change time ---> : {time.ctime(os.path.getctime(__file__))}', 'endWOinput')
	loader.writeLine('File size ----->  : ', 'endWOinput')
	loader.writeLine(f'In bytes ------> : {os.path.getsize(__file__)}', 'endWOinput')
	loader.writeLine(f'In kilobytes --> : {os.path.getsize(__file__) / 1000}', 'endWOinput')
	loader.writeLine(f'In megabytes --> : {os.path.getsize(__file__) / 1000000}', 'endWOinput')
	loader.writeLine(f'In gigabytes --> : {os.path.getsize(__file__) / 1000000000}', 'endWOinput')
	loader.writeLine(f'In terabytes --> : {os.path.getsize(__file__) / 1000000000000}', 'endWOinput')
	loader.writeLine(f'In petabytes --> : {os.path.getsize(__file__) / 100000000000000}', 'endWOinput')


def pathing(option):
    if option == 'dirPath':
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return dir_path
    elif option == 'SaveGames':
        dir_path = os.path.dirname(os.path.realpath(__file__))
        savePath = dir_path + '/SaveGames'
        return savePath


if __name__ == '__main__':
    main()
