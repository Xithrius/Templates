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
    algorithm(x)


def algorithm(x):
    
    return ', '.join(str(y) for y in x)

x = input('Numbers: ')
main(x)
