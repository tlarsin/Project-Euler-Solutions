# Tristan Larsin
# 7 - 23 - 17
# Find the sum of the even valued Fibonacci numbers that don't exceed 4,000,000

import sys
import os

def init():
    fibList = []
    count = 1
    start = 1

    fib1 = 0
    fib2 = 0
    sumVal = 0

    upperBound = 4000000

    while(sumVal < upperBound ):
        i = len(fibList) - 1
        val = 0

        if(i + 1 < 2):
            fibList.append(1)
        if(i + 1 < 3):
            fibList.append(2)
        else:
            val += fibList[i] + fibList[i - 1]
            fibList.append(val)

        if(fibList[i - 1] % 2 == 0):
            sumVal += fibList[i - 1]

    print('Sum of even values ' + str(sumVal))

init()
