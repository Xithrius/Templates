import pyautogui
pyautogui.FAILSAFE = True
import time
import math

'''
pyautogui.moveTo(x, y, duration=num_seconds)  # move mouse to XY coordinates over num_second seconds
pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)  # move mouse relative to its current position
pyautogui.moveTo(960, 540, duration=2)  # move mouse to XY coordinates over num_second seconds
pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=1, button='left')
'''

def main():
    pyautogui.moveTo(x=350, y=350, duration=0.5)
    for i in range(1, 30):
        pyautogui.dragRel(xOffset=(i * 10), duration=(0.5 / i))
        pyautogui.dragRel(yOffset=(i * 10), duration=(0.5 / i))
        pyautogui.dragRel(xOffset=(i * -10), duration=(0.5 / i))
        pyautogui.dragRel(yOffset=(i * -10), duration=(0.5 / i))
        pyautogui.moveRel(xOffset=math.sqrt(200), yOffset=math.sqrt(200), duration=0.5)


main()
