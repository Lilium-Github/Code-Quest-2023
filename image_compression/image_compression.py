'''System Module'''
import sys
import decimal

def better_round(user_in, degree: str = "1.0"):
    '''Round Half Up'''
    return decimal.Decimal(user_in).quantize(decimal.Decimal(degree),rounding=decimal.ROUND_HALF_UP)

def convert(inval, minval, maxval):
    return 255 * ((inval - minval)/(maxval - minval)) 

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    val = int(sys.stdin.readline().rstrip())
    numbers = []

    for i in range(val):
        newNum = float(sys.stdin.readline().rstrip())
        numbers.append(newNum)

    minval = numbers[0]
    maxval = numbers[0]

    for index, val in enumerate(numbers):
        if val > maxval:
            maxval = val
        if val < minval:
            minval = val

    for index, val in enumerate(numbers):
        converted = convert(val, minval, maxval)

        print(better_round(converted, "1"))