import loader

import time
import json
import os
import distutils.dir_util

import subprocess
p = subprocess.Popen(['TransferProd.cmd'])


def main():
	generateFiles('genAll')
	In0 = loader.writeLine(f'Create new save? [Y/N]:', 'endWinputLibrary')
	if In0 == 'n':
		check = True
		while check:
			loader.writeLine
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
						else:
							check1 = False
					else:
						check1 = False


	if In0 == 'y':
		loader.writeLine('Creating new save...', 'EndWOinput')
		x = generateFiles('genNewSave')
		return x
		generateFileProperties()


def generateFiles(type):
	if type == 'genAll':
		try:
			distutils.dir_util.mkpath(pathing('SaveGames'))
		except FileExistsError:
			pass
	elif type == 'genNewSave':
		In = loader.writeLine('Enter Name:')
		In0 = loader.writeLine('Enter password for new save:')
		i = 0
		check = True
		while check:
			if os.path.exists(pathing('SaveGames') + f'\\save{i}.json') is False:
				with open(pathing('SaveGames') + f'\\save{i}.json', 'w') as f:
					x = {"Name": In, "Pass": In0, "Cookies": 1, "Buildings": 1}
					json.dump(x, f)
				check = False
			else:
				i += 1
		return x


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


class Objects:
	objects = main()
	cookies = objects['Cookies']
	buildings = objects['Buildings']
	name = objects['Name']


Objects()
