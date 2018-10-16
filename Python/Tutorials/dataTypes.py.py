# Numbers
#Ints (integers)
integer = 6
binaryInt = 0b1001  # == 9
octalInt = 0o43  # == 35
hexInt = 0xff0000  # == red

# Floats "decimals"
decimal = 4.2
exponential = 3.2e4  # == 3.2*10**4 == 32000

#Complex (a + bi)
complexNumber = complex(4, 6)  # 4 + 6i

# Strings
string1 = "Hello World"
# or
string2 = 'Hello World'

#Booleans (True or False)
boolean = True

# Data Structures (holds many things)
# Lists
l = [4, 2, 5.3]

'''
Properties
Mutable (you can change it)
example:
l[1] = 5
print(l)
>>> [4, 5, 5.3]
Ordered (maintains order)
'''

# Tuple
t = (4, 2, 5.3)

'''
Properties
Immutable (you can't change it)
example:
t[1] = 5
>>> ValueError
Ordered (maintains order)
'''

# Set
s = {4, 6, 2}

'''
Properties
Mutable (you can change it)
Unordered (doesn't maintain order)
'''

print(s)  # {2, 4, 6}

# Why use a set over a list?
# Quicker operations

'a' in l  # l is list, slower, ~0.32s per 1,000,000
'a' in s  # s is set, faster, ~0.12s per 1,000,000

# Further reading: https://docs.python.org/3.6/library/stdtypes.html#set

# Dictionaries
d = {'a': 4,
     False: 3,
     0: 's'}

# Lookup
d['a']  # == 4
d[False]  # == 3
d[0]  # == 's'

# d['s'] >> KeyError

# Assignment
# d[5] >> KeyError
d[5] = 4
d[5]  # == 4

################################################################################
# Functions

# Syntax
# def name (arg0, arg1, kwarg0=defaultValue0):


def testFunction(x, y):  # Takes x and y and prints sum
    print(x + y)


testFunction(4, 5)  # read as 'testFunction of 4 and 5'


def testFunction2(x, y, z=1):  # Takes x and y and prints sum times z, default 5
    print((x + y) * z)


testFunction2(4, 5)  # behaves the same

testFunction2(4, 5, z=3)  # behaves the same times 3

# Functions return values, which can be put into variables


def returnFunction(x, y):
    return x ** y


z = returnFunction(2, 3)  # z == 8

z0 = returnFunction(2, 3) / 4  # z0 == 2

print(z, z0)
