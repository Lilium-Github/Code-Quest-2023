import sys
import decimal

def better_round(user_in, degree: str = "1.0"):
    '''Round Half Up'''
    return decimal.Decimal(user_in).quantize(decimal.Decimal(degree),rounding=decimal.ROUND_HALF_UP)

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    spaces = []
    for val in line.split(SEPARATOR):
        spaces.append(val)

    toPrint = ""

    for index, value in enumerate(spaces):
        if value == "M":
            toPrint = toPrint + str(index+1) + " "

    print(toPrint[0:-1])
