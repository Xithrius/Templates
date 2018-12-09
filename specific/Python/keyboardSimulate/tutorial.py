import pyautogui
pyautogui.FAILSAFE = True
import sys
import time

'''
Sources:
https://pyautogui.readthedocs.io/en/latest/cheatsheet.html
'''

def ghostMouse():

	# pyautogui.moveTo(x, y, duration=num_seconds)  # move mouse to XY coordinates over num_second seconds
	# pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)  # move mouse relative to its current position
	# pyautogui.moveTo(960, 540, duration=2)  # move mouse to XY coordinates over num_second seconds
	#pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=1, button='left')
	pass

def ghostType():

	pyautogui.hotkey('alt', 'tab')
	for i in 'quick brown fox':
		pyautogui.press(i)
	#typewrite('quick brown fox')


def clicker():

	check = True
	while check:
		clicksNumber = input('clicks: ') #int
		intervalTime = input('interval: ') #float
		if clicksNumber.isalpha():
			check = True
			print('No symbols or letters allowed')
		else:
			check = False
			clicksNumber = int(clicksNumber)
		if intervalTime.isalpha():
			check = True
			print('No symbols or letters allowed')
		else:
			check = False
			intervalTime = float(intervalTime)


	pyautogui.moveTo(300, 500, duration=2)
	for i in range(clicksNumber):
		pyautogui.click(clicks=1, button='left')
		print(f'{i} clicks complete', end='\r', flush=True)
		time.sleep(intervalTime)

#clicker()

def ghostScroll():
  # pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY)
	pyautogui.scroll(100, y=-1)
	pyautogui.scroll(10, y=1)


def ghostHoldDown():
#pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')
#pyautogui.mouseUp(x=moveToX, y=moveToY, button='left')
	pyautogui.mouseDown(x=100, y=100, button='left')


def ghostAlert():
	pyautogui.alert('Ya hecked up')


def trackPos():
	print('Press Ctrl-C to quit.')
	try:
		while True:
			x, y = pyautogui.position()
			print(x, y, end='\r')
			if x == 0:
				pyautogui.hotkey('ctrl', 'c')
	except KeyboardInterrupt:
		print('\n')


# trackPos()

def passwordTest():
	pyautogui.password(text='Test text', title='Test title', default='', mask='*')

passwordTest()
