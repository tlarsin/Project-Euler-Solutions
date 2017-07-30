# Tristan Larsin
# 7 - 29 - 17
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

import sys
import os

def init():
    valList = []
    sum = 0
    digits = ''

    with open('number.txt', 'r') as myfile:
        valList += myfile.readlines()

    for x in range(len(valList)):
        sum += int(valList[x])

    sumStr = str(sum)
    i = 0
    for ch in sumStr:
        i += 1
        if i < 11:
            digits += ch

    print('First 10 digits of sum: ' + str(digits))

init()
