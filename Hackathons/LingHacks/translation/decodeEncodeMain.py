import binary
import flipMove

# encode -> binary <- decode

# decode/encode

def language():

    language = input('binary, flipMove: ')

    if 'binary'.startswith(language.lower()):
        if binary.question():
            print('done')
    if 'flipMove'.startswith(language.lower()):
        flipMove()

language()
