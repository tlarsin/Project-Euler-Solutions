# Tristan Larsin
# 7 - 8 - 17
# Finds the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

import sys
import os


def init():
    count = 101
    val1 = 0
    val2 = 0
    sumOfNaturalNumbers = 0
    SquareOfSumOfNaturalNumbers = 0
    sumOfSquares = 0
    while(count > 0):
        count -= 1

        sumOfNaturalNumbers += count
        sumOfSquares += count * count

    difference = (sumOfNaturalNumbers * sumOfNaturalNumbers) - sumOfSquares
    print("Difference: " + str(difference))

init()
