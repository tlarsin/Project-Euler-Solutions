# Tristan Larsin
# 7 - 23 - 17
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

import sys
import os

def init():
    with open('number.txt', 'r') as myfile:
        val = myfile.read().replace('\n', '')


    strVal = str(val)
    integers = []
    largest = 0
    temp = 1
    for ch in strVal:
        integers.append(int(ch))

    for x in range(len(integers)):
        if(len(integers) - x > 13):
            for y in range(13):
                temp *= integers[x + y]
                if temp > largest:
                    largest = temp
            temp = 1

    print('Largest adjacent 13 digit product: ' + str(largest))

init()
