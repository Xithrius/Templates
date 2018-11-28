def main(x):
    print(x)
    x[0:14] = ''
    if x[0:4] == 'help':
        print(f"0:4 = {x[0:4]}")
        help = ''.join(str(y) for y in x)
        print(f"help: {help}")
        return help
    for i in range(len(x)):
        if x[i] == ',':
            if x[i + 1] == ' ':
                status = x[0:i]
                desc = x[i + 2:]
                status = ''.join(str(r) for r in status)
                desc = ''.join(str(r) for r in desc)
                return [status, desc]
                break
