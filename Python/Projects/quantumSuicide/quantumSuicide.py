# Quantum suicide v5
# How long will you last?

import time
import random
import json
import os

def main():
	deaths = 0
	bestChance = 1
	go = True
	while go:
		chance = 1
		i = 0
		while random.random() < 0.5:
			i += 1
			chance *= 0.5
			print(f'Survived: {i}, Chance: {chance}')
		deaths += 1
		print(f'Restarting, Deaths:    {deaths}')
		if deaths == 1000000:
			time.sleep(10)
		if chance < bestChance:
			bestChance = chance
	if KeyboardInterrupt is False:
		go = False
		print(f'Total Deaths: {deaths}, Best: {bestChance}')


'''
def pathing(option):
    if option == 'dirPath':
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return dir_path
'''
main()
