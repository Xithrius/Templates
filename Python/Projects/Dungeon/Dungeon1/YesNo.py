# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 21:55:38 2017

@author: Xithrius
"""


def yesNo(prompt):
    x = input(prompt + ' [Y/n]: ')
    valid = isValid(x)
    while valid is None:
        x = input(prompt + ' [Y/n]: ')
        valid = isValid(x)
    return valid


def isValid(x):
    if isYes(x):
        return True
    elif isNo(x):
        return False
    else:
        return None


def isYes(value):
    value = str(value).lower()
    return value in ['y', 'ye', 'yes']


def isNo(value):
    value = str(value).lower()
    return value in ['n', 'no']
