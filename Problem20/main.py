# Tristan Larsin
# 7 - 24 - 17
# Find the sum of the digits in the number 100!
import sys
import os

def init():
    count = 100
    val = 1
    sumDigits = 0
    i = 0

    while(count > 0):
        val *= count
        count -= 1

    val = str(val)

    for ch in val:
        sumDigits += int(ch)

    print("Sum of digits of 100! : " + str(sumDigits))


init()
