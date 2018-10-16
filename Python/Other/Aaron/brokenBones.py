# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:36:31 2017

@author: Xithrius
"""

import random

'''
If chuck is present, Aaron's bones are broken
If chuck is not present, Aaron breaks his own bones.
'''

r1String = random.randint(0, 1)
r1 = int(r1String)
d1 = {0: 'Chuck is there',
      1: 'Chuck is not there',
      }
d2 = {0: 'Aaron has bones for another day',
      1: 'Aarons bones are broken'
      }

if r1 == 0:
    x = d2[1]
    y = d1[0]

if r1 == 1:
    x = d2[0]
    y = d1[1]

print(y, 'and', x)
