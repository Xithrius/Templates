# aversion main

import time

def skull(string):
    skull = {1:'------------------------------------------------------------------',
             2:'----------------------██████████████████████----------------------',
             3:'-----------------████████████████████████████████-----------------',
             4:'------------██████████████████████████████████████████------------',
             5:'----------██████████████████████████████████████████████----------',
             6:'----------██████████████████████████████████████████████----------',
             7:'-------████████████████████████████████████████████████████-------',
             8:'-------████████████████████████████████████████████████████-------',
             9:'-----████████████████████████████████████████████████████████-----',
             10:'-----████████████████████████████████████████████████████████-----',
             11:'-----████████████████████████████████████████████████████████-----',
             12:'---████████████████████████████████████████████████████████████---',
             13:'---████████████████████████████████████████████████████████████---',
             14:'---████████████████████████████████████████████████████████████---',
             15:'---██████████████----████████████████████████----██████████████---',
             16:'---██████████████--------████████████████--------██████████████---',
             17:'---██████████████------------████████------------██████████████---',
             18:'----███████████-----------------██-----------------███████████----',
             19:'----██████████████████████████████████████████████████████████----',
             20:'----██████████████████████████████████████████████████████████----',
             21:'----██████████████████████████████████████████████████████████----',
             22:'------█████████████████████████-██-█████████████████████████------',
             23:'------████████████████████████--██--████████████████████████------',
             24:'------███████████████████████---██---███████████████████████------',
             25:'--------██████████████████████████████████████████████████--------',
             26:'--------------██████████████████████████████████████--------------',
             27:'---------------████████████████████████████████████---------------',
             28:'---------------████████████████████████████████████---------------',
             29:'---------------█████-----████████████████-----█████---------------',
             30:'------------█-------------██████████████-------------█------------',
             31:'-----------██----------------------------------------██-----------',
             32:'-----------███-------█----------------------█-------███-----------',
             33:'---------█████------██----------------------██------█████---------',
             34:'-----------███-███████----------------------███████-███-----------',
             35:'-------------██████████--------------------██████████-------------',
             36:'----------------█████████----------------█████████----------------',
             37:'--------------------██████████████████████████--------------------',
             38:'------------------------██████████████████------------------------',
             39:'---------------------------████████████---------------------------',
             40:'------------------------------------------------------------------'}

    if string == 'appear':
        for i in range(40):
            writeLine('------------------------------------------------------------------', 'n')

def writeLine(string, option, t=0.001):

    if option == 'n':
        for i in string:
            print(i, end='', flush=True)
            time.sleep(t)
        print(end='\n')

    if option == 'r':
        for i in string:
            print(i, end='\r', flush=True)
            time.sleep(t)

    elif option == 'none':
        for i in string:
            print(i, flush=True)
            time.sleep(t)

skull('appear')
