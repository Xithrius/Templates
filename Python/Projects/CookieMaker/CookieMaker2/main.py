import loader

import time
import json
import os
import distutils.dir_util


def main():
	generateFiles('genAll')
	In0 = loader.writeLine(f'Create new save? [Y/N]:', 'endWinputLibrary')
	if In0 == 'n':
		check = True
		while check:
			name = loader.writeLine('Name:')
			password = loader.writeLine('Enter password:')
			check1 = True
			i = 0
			while check1:
				with open(pathing('SaveGames') + f'\\Save{i}.json', 'r') as f:
					objects = json.load(f)
					if objects['Name'] == name:
						if objects['Pass'] == password:
							loader.writeLine(f'This save has {objects["Cookies"]} cookie(s), and {objects["Buildings"]} building(s)', 'endWOinput')
							In1 = loader.writeLine('Is this correct? [Y/N]:')
							if In1 == 'y':
								pass
							elif In1 == 'n':
								pass
						else:
							check1 = False
					else:
						check1 = False


	if In0 == 'y':
		loader.writeLine('Creating new save...', 'EndWOinput')
		generateFiles('genNewSave')
		generateFileProperties()
		#saveDecision()


class objects:
	cookies = 0
	buildings = 0
	if cookies != 0:
		print(cookies)


def generateFiles(type):
	if type == 'genAll':
		try:
			distutils.dir_util.mkpath(pathing('SaveGames'))
		except FileExistsError:
			pass
	elif type == 'genNewSave':
		i = 0
		check = True
		while check:
			try:
				with open(pathing('SaveGames') + f'\\save{i}.json') as f:
					In0 = loader.writeLine('Enter Name:')
					In = loader.writeLine('Enter password for new save:')
					x = {"Name": In0, "Pass": In, "Cookies": 0, "Buildings": 0}
					check = False
					json.dump(x, f) # ERROR
			except FileExistsError:
				i += 1


'''
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
'''


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
        savePath = dir_path + '\\SaveGames'
        return savePath

main()
