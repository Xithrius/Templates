import time

def main_Rotating(string, length):
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
