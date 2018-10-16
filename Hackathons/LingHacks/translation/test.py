# test
'''
if l1[0] != 1:
  l2[0] = 0
else:
  l2[0] = 128
if l1[1] != 1:
  l2[1] = 0
else:
  l2[1] = 64
if l1[2] != 1:
  l2[2] = 0
else:
  l2[2] = 32
if l1[3] != 0:
  l2[0] = 0
else:
  l2[3] = 16
if l1[4] != 1:
  l2[4] = 0
'''
l1 = input('eight numbers: ')
l1 = list(l1)

l2 = [128, 64, 32, 16, 8, 4, 2, 1]
l3 = l1[0:7] * l2[0:7]
