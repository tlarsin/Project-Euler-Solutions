# Tristan Larsin
# 7 - 24 - 17
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.



import sys
import os

def init():
    digits = []
    lastTenDigits = ''

    power = 0
    for a in range(1, 1000):
        power += a ** a

    for ch in str(power):
        digits.append(ch)

    for a in range(len(digits) - 10, len(digits)):
        lastTenDigits += str(digits[a])

    print('Last 10 digits: ' + str(lastTenDigits))

init()
