'''
0123

n! = 1*2*...*(n-1)*n
4! = 1*2*3*4

***
n! = n*(n-1)!
***

n!  1  2  6 24
n   1  2  3  4

4! = 24
3! = 6

n! = n*(n-1)!
4! = 4*3!

3! = 3*2!

0123
0132

0213
0231

0312
0321

1023
1203
1302
1032
1230
1320

2130
2031
2013
2103
2301
2310

3210
3120
3021
3201
3102
3012

***
0123
1023
2013
0213
1203
2130
2103
1230
3210
2310
1320
3120
3021
0321
2301
3201
0231
2031
1032
0132
3102
1302
0312
3012
***

4 items = 24 permutations


012

012
102
201
021
120
210

3 items = 6 permutations

01

01
10

2 items = 2 permutations


0

0

1 item = 1 permutation
'''

e = end number
s = start number
f = first number

# 1: a
# 2: b
# 3: c
# 4: d
# 5: e
# 6: f

N_i = i + 1 - S = 6
N_j = j + 1 - S = 4

N_ij = N_j - N_i + 1 = j - i + 1

e = 2
s = 1
f = 1

I = 2

I = e - s + f



# 2: a
# 3: b
# 4: c

S  offset
0  1
1  0
2  -1
14 -13

offset = 1 - S
N = i + offset

N = i + 1 - S

'''
 *** permutations ***
 ***

function permutations (items)
    if number of items > 1
        for i in items
            yield all of i + permutations(items without i)
    else
        return item

def permutations(items):
    if len(items) > 1:
        perms = []
        for perm in permutations(items without i):
            perms.append(i + perm)
        return perms
    return items

permutations (0, 1, 2, 3) {
    i = 2
    [(0, 1, 2, 3) (0, 1, 3, 2) (0, 2, 1, 3) (0, 2, 3, 1), (0, 3, 1, 2), (0, 3, 2, 1)
    (1, 0, 2, 3), (1, 0, 3, 2), (1, 2, 0, 3), (1, 2, 3, 0), (1, 3, 0, 2), (1, 3, 2, 0)
    ]
}

permutations (0, 1, 3) {
    i = 1
    [(0, 1, 3), (0, 3, 1)]
}



01234
120

01234
01243
01324
01

234
243
324
342
423
432











'''

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
