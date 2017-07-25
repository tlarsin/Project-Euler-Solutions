# Tristan Larsin
# 7 - 24 - 17
# What is the sum of the digits of the number 21000?
import sys
import os

def init():
    val = 2 ** 1000
    sumDigits = 0

    valStr = str(val)
    for ch in valStr:
        sumDigits += int(ch)

    print("Sum of digits of 2 ^ 1000: " + str(sumDigits))

init()
