#only/just Monika

from random import randint
from time import sleep


def main():
    while True:
        x = randint(0, 1)
        if x == 1:
            writeLine("Just Monika")
        else:
            writeLine("Only Monika")


def writeLine(string):
    for i in string:
        print(i, end='\r', flush=True)
        sleep(0.01)


main()
