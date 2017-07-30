# Tristan Larsin
# 7 - 30 - 17
# Find the sum of all the primes below two million

import sys
import os

def init():
    i = 1
    sum =  0

    upperBound = 2000000

    while(i < upperBound):
        i += 1

        if isPrime(i):
            sum += i

    print('Sum of primes below 2 million ' + str(sum))

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
