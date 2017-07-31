# Tristan Larsin
# 7 - 30 - 17
# What is the value of the first triangle number to have over five hundred divisors?

import sys
import os
import math

def init():
    sumVal = count = i = 0
    prod = 1


    while(i < 500):
        temp = 1
        i = 0

        count += 1
        sumVal += count

        for x in range(1, int(math.sqrt(sumVal))):
            test = sumVal % x

            if test == 0:
                i += 1

        prod = 1
        i *= 2

    print('First triangle number with over 500 divisors: ' + str(sumVal) + ' has ' + str(i) + ' divisors')

init()
