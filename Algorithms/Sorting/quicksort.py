def main(x):
    check = True
    while check:
        x = list(x)
        for i in range(len(x)):
            if x[i].isdigit():
                x[i] = int(x[i])
                if i == len(x) - 1:
                    check = False
                    break
            else:
                print(f"{x[i]} and other possibly similar inputs are not acceptable")
                check = True
    check = True
    pivot = x[len(x) - 1]
    while check:
        x = algorithm(x)



def algorithm(x):
    pivot = x[len(x) - 1]
    for i in range(len(x) - 1):
        if pivot < x[len(x) - 2]:
            x[len(x) - 2], pivot = pivot, x[len(x) - 2]

x = input('Numbers: ')
main(x)
