import time
from random import choice


def main():
    In = writeLine('Input:', 0.01)
    In = list(In)
    spaceList = []
    In.insert(0, ' ')
    In.insert(len(In), ' ')
    for i in range(len(In)):
        if In[i] == ' ':
            spaceList.append(i)
    wordList = []
    for i in range(len(spaceList) - 1):
        word = In[spaceList[i]:spaceList[i + 1]]
        word.remove(' ')
        state = choice([0, 1, 2, 3, 4])
        if state == 1:
            firstLetter = word[0]
            firstLetter = f'{firstLetter}-'
            word.insert(0, firstLetter)
            word.insert(len(word), ' ')
            word = ''.join(str(e) for e in word)
        elif state == 2:
            firstLetter = word[0]
            firstLetter = f'{firstLetter}-{firstLetter}-'
            word.insert(0, firstLetter)
            word.insert(len(word), ' ')
            word = ''.join(str(e) for e in word)
        else:
            word.insert(len(word), ' ')
            word = ''.join(str(e) for e in word)

        wordList.append(word)
    wordList = ''.join(str(e) for e in wordList)
    print(wordList)


def writeLine(string, t):
    for i in string:
        print(i, end='', flush=True)
        time.sleep(t)
    In = input(' ')
    return In

main()
