import time
def main():
    number = 1
    x = [1, 1]
    i = 0
    while True:
        x.insert((i + 1), (x[i - 1] + x[i]))
        writeLine(f"█ Row {number} █ {x[i]}")
        i += 1
        number += 1


def writeLine(string):
    for i in string:
        print(i, end='', flush=True)
        time.sleep(0.1)


main()
