def main(x):
    x[0:14] = ''
    check = x[0:4]
    if ''.join(str(y) for y in check) == 'Help':
        return [''.join(str(y) for y in check), '']
    elif ''.join(str(y) for y in check) != 'Help':
        for i in range(len(x)):
            if x[i] == ',':
                if x[i + 1] == ' ':
                    status = x[0:i]
                    desc = x[i + 2:]
                    status = ''.join(str(r) for r in status)
                    desc = ''.join(str(r) for r in desc)
                    return [status, desc]
                    break
