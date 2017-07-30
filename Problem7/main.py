# Tristan Larsin
# 7 - 30 - 17
# Finds the 10001st prime value

import sys
import os

def init():
    count = i = 0

    while(count < 10002):
        i += 1
        if isPrime(i):
            count += 1

    print('10001st prime: ' + str(i))

# A prime (except 2 and 3) is of form 6k - 1 or 6k + 1
# Primality test credit goes to Alexandru on Stack Overflow
def isPrime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

init()
