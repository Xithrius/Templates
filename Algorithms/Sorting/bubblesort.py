def main(x):
    check = True
    while check:
        x = list(x)
        for i in range(len(x)):
            try:
                x[i] = int(x[i])
                if i == len(x) - 1:
                    algorithm(x)
                    check = False
                    break
            except:
                print(f"{x[i]} and other possibly similar inputs are not acceptable")
                x = input('Numbers: ')
                check = True


def algorithm(x):
    check = True
    while check:
        check = False
        for i in range(len(x) - 1):
            if x[i] > x[i + 1]:
                x[i], x[i + 1] = x[i + 1], x[i]
                check = True
                print(x)
x = input('Numbers: ')
main(x)
