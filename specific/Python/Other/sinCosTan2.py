# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 20:27:38 2017

@author: Xithrius
"""

import math


def main():
    mode = input('mode (sin, cos, tan): ')
    assert mode in ['sin', 'cos', 'tan'], 'Invalid mode'
    opp = input('Opposite side (empty for unknown): ')
    adj = input('Adjacent side (empty for unknown): ')
    hyp = input('Hypotenuse side (empty for unknown): ')
    sides = [opp, adj, hyp]
    for i, side in enumerate(sides):
        try:
            if side == '':
                sides[i] = None
            elif side.lower() in ['inf', '-inf', 'nan', '-nan']:
                raise ValueError()
            else:
                sides[i] = float(side)
        except ValueError:
            print('Invalid side "' + side + '"')
            return
    noneCount = 0
    for side in sides:
        if side is None:
            noneCount += 1
    if noneCount != 1:
        print('Incorrect number unknowns specified')
        return
    #sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2
    if sides[0] is None:
        sides[0] = math.sqrt(sides[2] ** 2 - sides[1] ** 2)
    if sides[1] is None:
        sides[1] = math.sqrt(sides[2] ** 2 - sides[0] ** 2)
    if sides[0] is None:
        sides[0] = math.sqrt(sides[0] ** 2 - sides[1] ** 2)

    divisions = {'sin': (0, 2),
                 'cos': (1, 2),
                 'tan': (0,1)}

    div = divisions[mode]

    if mode == 'sin':
        print(sides[0] / sides[2])
    elif mode == 'cos':
        print(sides[1] / sides[2])
    elif mode == 'tan':
        print(sides[0] / sides[1])

    print(sides)


main()
