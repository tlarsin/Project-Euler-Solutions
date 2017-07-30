# Tristan Larsin
# 7 - 30 - 17
# What is the largest prime factor of the number 600851475143 ?

import sys
import os

def init():
    i = largest =  0
    temp = 1

    primes = []

    val = 600851475143

    while(temp != val):
        i += 1
        temp = 1

        if val % i == 0 and isPrime(i):
            if i > largest:
                largest = i
                primes.append(largest)

                for x in range(len(primes)):
                    temp *= primes[x]

    print('Largest prime factor ' + str(largest))

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
