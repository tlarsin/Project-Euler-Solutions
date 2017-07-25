# Tristan Larsin
# 7 - 24 - 17
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import sys
import os

def init():
    fibList = []
    digitCount = 0

    while(1):
        i = len(fibList) - 1
        val = 0

        if(i + 1 < 1):
            fibList.append(1)
        if(i + 1 < 2):
            fibList.append(2)
        else:
            val += fibList[i] + fibList[i - 1]
            fibList.append(val)

        valStr = str(fibList[i])

        for ch in valStr:
            digitCount += 1

        if(digitCount == 1000):
            print('Index of first term to contain 1000 digits: ' + str(len(fibList)))
            break

        digitCount = 0
init()
