# Tristan Larsin
# 7 - 23 - 17
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


import sys
import os

def init():
    digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    double = [ 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    hundred = ['hundred']
    thousand = ['thousand']
    extend = 'and'

    start = 1
    count = 0
    total = 0
    digit = []

    while(start < 1001):
        startStr = str(start)
        digit = []

        count = 0

        for ch in startStr:
            count += 1
            digit.append(ch)

        # 1 digit number
        if count == 1:
            total += len(digits[int(digit[0])])

        # 2 digit number
        if count == 2:
            if digit[0] == '1':
                total += len(tens[int(digit[1])])

            else:
                # If second digit isn't 0 add more letters
                if digit[1] != '0':
                    total += len(double[int(digit[0]) - 2])
                    total += len(digits[int(digit[1])])

                # second digit is a 0
                else:
                    total += len(double[int(digit[0]) - 2])

        # 3 digit number
        if count == 3:
            # First digit
            total += len(digits[int(digit[0])])

            # Hundred
            total += len(hundred[0])

            # If second digit is 1 then add from tens list
            if digit[1] == '1':
                total += len(tens[int(digit[2])])
                total += len(extend)
            # otherwise find
            else:
                # If second digit isn't 0 add more letters
                if digit[1] != '0':
                    total += len(double[int(digit[1]) - 2])
                    total += len(extend)

                    # if third digit isn't 0 find the digit
                    if digit[2] != '0':
                        total += len(digits[int(digit[2])])

                # second digit is 0 so find the third digit
                else:
                    # if third digit isn't 0 then do nothing
                    if digit[2] != '0':
                        total += len(digits[int(digit[2])])
                        total += len(extend)


        # 4 digit number
        if count == 4:
            total += len(digits[1])
            total += len(thousand[0])

        start += 1

    print('Total characters from numbers 1 - 1000 (inclusive): ' + str(total))

init()
