# Tristan Larsin
# 7 - 30 - 17
# Which starting number, under one million, produces the longest chain?

import sys
import os
import math

def init():
    start = 0
    largestChainSum = 0
    val = 0

    chain = []

    upperBound = 999999


    while(start < upperBound):
        start += 1
        chain = []

        temp = start
        chain.append(temp)

        while(temp != 1):
            if temp % 2 == 0:
                temp = temp / 2 # n -> n / 2 (n is even)
                chain.append(temp)
            else:
                temp = (3 * temp) + 1 # n-> 3n + 1 (n is odd)
                chain.append(temp)

        if len(chain) > largestChainSum:
            val = start
            largestChainSum = len(chain)

        if(start % 10000 == 0):
            print('Computing ' + str(start))

    print(str(val) + ' produces the largest chain at ' + str(largestChainSum) + ' items')

init()
