# my own language with encoding/decoding

'''
example
pleexam
maxeelp
'''

def encode():

    e = input('Encode: ')
    print('Encoding...')

    if encodeAlgorithm(e):
        return True


def decode():

    d = input('Decoding: ')
    print('Decoding...')

    if decodeAlgorithm(d):
        return True

'''
example
    ^^^
pleexam
^^^
'''

def encodeAlgorithm(e):
    e = list(e)
    l1 = e[0:(len(e) / 2)]
    e.insert(l1)

    print(e)


def decodeAlgorithm(d):
    d = list(d)

    print(d)
