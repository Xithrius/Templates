'''
dunder = d (double) + under (underscore)
ex:
__init__
__str__
__add__
'''
from math import sqrt

class Car:
    def __init__(self, topSpeed, name):
        self.topSpeed = topSpeed
        self.name = name

    def __repr__(self):
        return f'Car({self.topSpeed}, {self.name})'

    def __str__(self):
        return f'{self.name} can go {self.topSpeed} mph'


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'<{self.x}, {self.y}>'

    #sqrt(x**2 + y**2)
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


tim = Car(100, 'Timmy')

print(tim)
print(repr(tim))

vec0 = Vector(3, 4)
vec1 = Vector(1, -2)

print(vec0 + vec1)

l = abs(vec0)

print(l)

x = 5
y = 10

# '5 + 10 = 15'
print(str(x) + ' + ' + str(y) + ' = ' + str(x + y))
print('%i + %i = %i' % (x, y, x + y))
print(f'{x} + {y} = {x + y}') ### BEST ###
