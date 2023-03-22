import sys
import decimal

def better_round(user_in, degree: str = "1.0"):
    '''Round Half Up'''
    return decimal.Decimal(user_in).quantize(decimal.Decimal(degree),rounding=decimal.ROUND_HALF_UP)

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip().split(" ")

    smallBricks = int(line[0])
    largeBricks = int(line[1])
    x = int(line[2])

    done = False

    while not done:
        if x < 5:
            if smallBricks > 0:
                smallBricks += -1
                x += -1
            else:
                done = True
                solved = False
        elif x >= 5:
            if largeBricks > 0:
                largeBricks += -1
                x += -5
            elif smallBricks > 0:
                smallBricks += -1
                x += -1
            else:
                done = True
                solved = False
        
        if x == 0:
            done = True
            solved = True

    print(str(solved).lower())
