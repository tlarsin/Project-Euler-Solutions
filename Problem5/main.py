# Tristan Larsin
# 7 - 8 - 17
# Finds the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

import sys
import os

def init():
    val = 0
    currentVal = 20
    count = 0
    valFound = 0

    while(valFound == 0):
        i = 2
        count = 0
        currentVal += 10
        if(currentVal % i == 0):
            count += 1
            while(i < 21):
                if(currentVal % i == 0):
                    count += 1
                else:
                    break
                if(count == 20):
                    valFound = 1
                    val = currentVal
                i += 1

        print('current val: ' + str(currentVal))
    print('Smallest value is ' + str(val))

init()
