# Tristan Larsin
# 7 - 23 - 17
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

import sys
import os

def init():
    for a in range(1, 1001):
        for b in range(a + 1, 1001):
            c = 1000 - a - b
            if(a * a + b * b == c * c):
                print('a ' + str(a) + ' b ' + str(b) + ' c ' + str(c))
                print("a*b*c = " + str(a * b * c))


init()
