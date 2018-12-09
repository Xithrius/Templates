check = True
while check:
    x = input('Input numbers: ')
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
while check:
    check = False
    for i in range(len(x) - 1):
        if x[i] > x[i + 1]:
            x[i], x[i + 1] = x[i + 1], x[i]
            check = True
            print(f"{x}")

print(f"{x}")
