# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 21:55:38 2017

@author: Xithrius
"""


def upDownLeftRight(prompt):
    x = input(prompt + ' [U/D/L/R]: ')
    valid = isValid(x)
    while valid is None:
        x = input(prompt + ' [U/D/L/R]: ')
        valid = isValid(x)
    return valid


def isValid(x):
    if isUp(x):
        return 90
    if isDown(x):
        return 270
    if isLeft(x):
        return 180
    elif isRight(x):
        return 0
    else:
        return None


def isUp(value):
    value = str(value).lower()
    return value in ['u', 'up']


def isDown(value):
    value = str(value).lower()
    return value in ['d', 'do', 'dow', 'down']


def isLeft(value):
    value = str(value).lower()
    return value in ['l', 'le', 'lef', 'left']


def isRight(value):
    value = str(value).lower()
    return value in ['r', 'ri', 'rig', 'righ', 'right']
