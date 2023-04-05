import sys
import decimal

def better_round(user_in, degree: str = "1.0"):
    '''Round Half Up'''
    return decimal.Decimal(user_in).quantize(decimal.Decimal(degree),rounding=decimal.ROUND_HALF_UP)

SEPARATOR = ", "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    
    sides = []
    
    for val in line.split(SEPARATOR):
        sides.append(int(val))

    sides.sort()

    if sides[2] >= sides[0] + sides[1]:
        print("Not a Triangle")
    elif sides[0] == sides[2]:
        print("Equilateral")
    elif sides[0] == sides[1] or sides[1] == sides[2]:
        print("Isosceles")
    else:
        print("Scalene")