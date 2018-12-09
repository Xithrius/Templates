# movement can cause death
# Dungeon V 0


import math
import random
import time

import YesNo
import upDownLeftRight


def Dungeon():

    if YesNo.yesNo('Would you like to enter the dungeon?'):
        print('Entering dungeon...')
        time.sleep(2.5)

        r0 = random.randint(15, 30)

        t0 = 0.9
        for i in range(0, r0):
            print('falling...')
            time.sleep(t0)
            t0 = t0 - 0.025

        if 0 < random.randint(0, 100) < 75:
            print("You survived the fall")
            if upDownLeftRight.upDownLeftRight('Which direction would you like to go?') is 90:
                if directionSituation(10):
                    print('test complete')

        else:
            print("You didn't survive the fall")
            if Life(10):
                pass
            else:
                quit()

    else:
        time.sleep(0.1)
        print('q')
        time.sleep(0.1)
        print('u')
        time.sleep(0.1)
        print('i')
        time.sleep(0.1)
        print('t')
        time.sleep(0.1)
        print('t')
        time.sleep(0.1)
        print('i')
        time.sleep(0.1)
        print('n')
        time.sleep(0.1)
        print('g')
        time.sleep(0.1)
        t2 = random.randint(3, 10)
        for i in range(t2):
            print('.')
            time.sleep(0.1)
        time.sleep(4)
        quit()


def Life(x=0):

    life = 100

    if x > 0:
        life = life - x
        return True
        print('You lost', x, 'health, and', life, 'left')

    if life == 0:
        print('Y̶͈͈̋̽̇̌̈́̓̾͛͂͐̽͒̒̕͝ỏ̵̰̮̗͈̦͚̘͎̱̦͎̗͛̈́͌̚u̷̹̜͔̼͖̖̯̯͇̹͓̞͛̽̃ ̶̱̠̖͇̹̩̙̼̙͈͙͙̋́h̸͈̺̐ą̵̡̡̧̣͕̠̪͓͙̫̒̆̆v̶̢̻̘̱̹͎̣̻͖͑e̴̳̒̾͌̈ ̴̛̮̋͗̏̆͆͋̇̊̐̊̏̕̚d̶̲̔̓͊͗̾i̵̹̝͖̩̠͓̗͐̐̋̏̍̋́́̔͂̕͝e̶̪̻̘̗̊̌̈́̾̓̓̔̅͛̚͜͝͝ḑ̸̹͖̩̱͚̫̳͈̤̆̂̎͜')
        quit()


def directionSituation(x, y):

    if x == 0.5:
        x1 = float(random.random(x, y))
        if 0 <= x1 <= 0.5:
            pass


def lines(x):

    # event
    # question
    # yes event
    # no event

    # not bad
    d1 = {0: 'Crippling depression hits you.',
          1: 'Fight the depression?',
          2: 'Depression has lost its place; you killed it.',
          3: "You did not fight it, but it slowly fades away.",

          4: "You're not alone.",
          5: 'Turn around?',
          6: 'Nothing is there.',
          7: 'You run from the object in the darkness.',

          8: 'A cat sits in a doorway.',
          9: 'Pet the cat?',
          10: 'purrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr.',
          11: 'It walks back into the darkness.'}

    # just a little pinch
    d2 = {0: 'Something sits in the doorway.',
          1: 'Investigate?',
          2: "What's a turtle doing down here?",
          3: 'You walk away, but it ran up to you and bit your foot',

          4: 'You see something down the corridor.',
          5: 'Go to the UO?',
          6: "it's a plate. You pick it up, but a large rock tumbles down the corridor.",
          7: 'A rock tumbles toward you. No survivors.',

          8: 'A large insect sits in front of you.',
          9: 'Smash the little bugger?',
          10: 'You crush it, but a large amount of insects seek revenge',
          11: 'You step over it, just in case.'}

    # you shouldn't be stepping here
    d3 = {0: 'A humanoid figure stands in the doorway.',
          1: 'Ask its name?',
          2: 'You ask, but it does not reply.',
          3: 'You turn around and move on.',

          4: 'A alien-like figure stands in the doorway.',
          5: 'Interact with it?',
          6: 'You try to interact with it, but it is a shadow.',
          7: 'It starts moving toward you, but then through you.',

          8: 'You see a dog in the distance',
          9: 'Attempt to pet it?',
          10: 'You walk forward, but it runs toward you with rage in its eyes.',
          11: 'In the distance, the dog walks away'}

    # What are you doing down here, little human?
    d4 = {0: 'The ceiling begins to fall.',
          1: 'Try to run?',
          2: "You try to exist, but running wasn't enough.",
          3: 'Half of your body got stuck under the wall.',

          4: "Doors aren't supposed to exist in this place.",
          5: 'Open it?',
          6: 'You open the door, but a large hand takes you in.',
          7: 'You continue you adventure in a different direction',

          8: 'Many Humanoid objects begin to surround you',
          9: 'Run?',
          10: 'You try to break the circle, but they collapse on you.',
          11: 'They slowly dissapear, while you stand motionless.'}

    # You shouldn't exist
    d5 = {0: 'A large figure floats above the ground.',
          1: 'stay?',
          2: "You shouldn't have stayed.",
          3: 'It takes an impossibly long step and breaks your body.',

          4: 'You found a child facing away from you.',
          5: 'You probably should stay away...',
          6: 'The child turns around, revealing a face with no features. You should have ran.',
          7: 'You ran straight out of the dungeon, to reset it.',

          8: 'A face fills the doorway.',
          9: 'You want to look closer, but should you?',
          10: 'You walk up to it, but everything around you glitches and you fall into the void.',
          11: 'You turn around only to fall into the infinitly deep void.'}

    # The chances of escaping are slim
    dEscape = {0: 'Moving on...',
               1: 'Turning around...',
               2: 'Exiting this area...',
               3: 'Walking away...',
               4: 'jogging away...',
               5: 'running away...',
               6: 'Sprinting away...',
               7: 'Crawling away...',
               8: 'Sliding away...'}

    if x == 0:
        print(ValueError)

    if x == 1:
        z1 = random.random(0, 100)

        # d1 1
        if 0 < z1 < (1 / 3) * 100:
            print(d1[0])

            if YesNo.yesNo(d1[1]):
                print(d1[2])
                print(dEscape[random.randint(0, 2)])

            else:
                print(d1[3])
                if Life(5):
                    print(dEscape[random.randint(0, 3)])
                else:
                    pass

        # d1 2
        if (1 / 3) * 100 < z1 < (2 / 3) * 100:
            print(d1[4])

            if YesNo.yesNo(d1[5]):
                print(d1[6])
                print(dEscape[random.randint(0, 2)])

            else:
                print(d1[7])
                print(dEscape[random.randint(0, 3)])

        # d1 3
        if (2 / 3) * 100 < z1 <= 100:
            print(d1[9])

            if YesNo.yesNo(d1[9]):
                print(d1[10])
                print(dEscape[random.randint(0, 2)])

            else:
                print(d1[11])
                if Life(1):
                    print(dEscape[random.randint(0, 3)])
                else:
                    pass

    if x == 2:
        z2 = random.random(0, 100)

        # d2 1
        if 0 < z2 < (1 / 3) * 100:
            print(d2[0])

            if YesNo.yesNo(d2[1]):
                print(d2[2])
                print(dEscape[random.randint(0, 2)])

            else:
                print(d2[3])
                if Life(7):
                    print(dEscape[random.randint(0, 3)])
                else:
                    pass

        # d2 2
        if (1 / 3) * 100 < z2 < (2 / 3) * 100:
            print(d2[4])

            if YesNo.yesNo(d2[5]):
                print(d2[6])
                print(dEscape[random.randint(0, 2)])

            else:
                print(d2[7])
                print(dEscape[random.randint(0, 3)])

        # d2 3
        if (2 / 3) * 100 < z2 <= 100:
            print(d2[9])

            if YesNo.yesNo(d2[9]):
                print(d2[10])
                if Life(5):
                    print(dEscape[random.randint(4, 6)])
                else:
                    pass

            else:
                print(d1[11])
                print(dEscape[random.randint(0, 3)])

    if x == 3:
        z3 = random.random(0, 100)

        # d3 1
        if 0 < z3 < (1 / 3) * 100:
            print(d3[0])

            if YesNo.yesNo(d3[1]):
                print(d3[2])
                print(dEscape[random.randint(0, 4)])

            else:
                print(d3[3])
                print(dEscape[random.randint(2, 4)])

        # d3 2
        if (1 / 3) * 100 < z3 < (2 / 3) * 100:
            print(d3[4])

            if YesNo.yesNo(d3[5]):
                print(d3[6])
                print(dEscape[random.randint(0, 2)])

            else:
                print(d3[7])
                if Life(10):
                    print(dEscape[random.randint(5, 6)])
                else:
                    pass
        # d3 3
        if (2 / 3) * 100 < z3 <= 100:
            print(d3[9])

            if YesNo.yesNo(d3[9]):
                print(d3[10])
                if Life(20):
                    print(dEscape[random.randint(4, 6)])
                else:
                    pass

            else:
                print(d3[11])
                print(dEscape[random.randint(0, 3)])

    if x == 4:
        z4 = random.random(0, 100)

        # d4 1
        if 0 < z4 < (1 / 3) * 100:
            print(d4[0])

            if YesNo.yesNo(d4[1]):
                print(d4[2])
                if Life(100):
                    pass
                else:
                    pass

            else:
                print(d4[3])
                if Life(50):
                    print(dEscape[random.randint(2, 4)])

        # d4 2
        if (1 / 3) * 100 < z4 < (2 / 3) * 100:
            print(d4[4])

            if YesNo.yesNo(d4[5]):
                print(d4[6])
                print(dEscape[random.randint(0, 2)])

            else:
                print(d4[7])
                if Life(10):
                    print(dEscape[random.randint(5, 6)])
                else:
                    pass
        # d4 3
        if (2 / 3) * 100 < z4 <= 100:
            print(d4[9])

            if YesNo.yesNo(d4[9]):
                print(d4[10])
                if Life(20):
                    print(dEscape[random.randint(4, 6)])
                else:
                    pass

            else:
                print(d4[11])
                print(dEscape[random.randint(0, 3)])

    if x == 5:
        z5 = random.random(0, 100)

        # d4 1
        if 0 < z5 < (1 / 3) * 100:
            print(d4[0])

            if YesNo.yesNo(d4[1]):
                print(d4[2])
                if Life(100):
                    pass
                else:
                    pass

            else:
                print(d4[3])
                if Life(50):
                    print(dEscape[random.randint(2, 4)])

        # d4 2
        if (1 / 3) * 100 < z5 < (2 / 3) * 100:
            print(d4[4])

            if YesNo.yesNo(d4[5]):
                print(d4[6])
                print(dEscape[random.randint(0, 2)])

            else:
                print(d4[7])
                if Life(10):
                    print(dEscape[random.randint(5, 6)])
                else:
                    pass
        # d4 3
        if (2 / 3) * 100 < z5 <= 100:
            print(d4[9])

            if YesNo.yesNo(d4[9]):
                print(d4[10])
                if Life(20):
                    print(dEscape[random.randint(4, 6)])
                else:
                    pass

            else:
                print(d4[11])
                print(dEscape[random.randint(0, 3)])


Dungeon()
