# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:32:09 2017

@author: Xithrius
"""

import random

rString = random.randint(0, 3)
r = int(rString)
d = {0: 'screw you',
     1: 'frick you',
     2: 'flip you',
     3: 'razzel dazzel you'
     }
x = d[r]
print(x)
