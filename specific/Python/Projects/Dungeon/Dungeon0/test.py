# Dungeon test
def dic():
    d = {1: '0'
         }

    print(d[1])


def color():

    import colorsys
    from colorama import Fore

    colorama.init()

    print("You have", Fore.Red + "died")


color()
