import win32api
import PIL.ImageGrab

import datetime
import pytz


def getCurrColor(pos=None):
    x, y = pos
    if pos is None:
        x, y = win32api.GetCursorPos()
    grab = PIL.ImageGrab.grab((x, y, x + 1, y + 1))
    return grab.getpixel((0, 0))


pos = win32api.GetCursorPos()
color = getCurrColor(pos)

pst = pytz.timezone('US/Pacific')

while True:
    nextColor = getCurrColor(pos)

    if color != nextColor:
        print(datetime.datetime.now(pst))

    color = nextColor
