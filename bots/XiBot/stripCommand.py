def main(x):
    x[0:14] = ''
    for i in range(len(x)):
        if x[i] == ',':
            if x[i + 1] == ' ':
                status = x[0:i]
                desc = x[i + 2:]
    status = ''.join(str(y) for y in status)
    desc = ''.join(str(y) for y in desc)
    return [status, desc]