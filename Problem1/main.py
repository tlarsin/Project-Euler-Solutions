# Tristan Larsin
# 7 - 8 - 17
# Sums values < 1000 that are divisible by 3 or 5

import sys
import os

def init():
    count = 0
    totalSum = 0
    multipleCount = 1

    while(count < 1000):
        if((count % 3 == 0) or (count % 5 == 0) and (count % 1 == 0)):
            totalSum += count
            multipleCount += 1
            print("Divisible by 3 or 5:" + str(count))

        count += 1

    print("multipleCount: " + str(multipleCount))
    print("Total Sum: " + str(totalSum))

init()
