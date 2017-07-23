# Tristan Larsin
# 7 - 8 - 17
# Finds the largest palindrome created by the product of two 3 digit numbers

import sys
import os


def init():
    palindrome = 0
    largestPal = 0
    value1 = 1000
    value2 = 1000
    count = 0
    val = 0

    while(value1 > 99):
        value1 -= 1
        value2 = 1000
        while(value2 > 99):
            value2 -= 1
            palindrome = value1 * value2
            newPal = str(palindrome)
            if((len(newPal) % 2) == 0):
                firstpart, secondpart = newPal[:int(len(newPal)/2)], newPal[int(len(newPal)/2):]
                newVal = secondpart[::-1]
                if(firstpart == newVal):
                    if(largestPal < palindrome):
                        largestPal = palindrome
                        print("Largest" + str(largestPal))


init()
