import sys
import decimal

def better_round(user_in, degree: str = "1.0"):
    '''Round Half Up'''
    return decimal.Decimal(user_in).quantize(decimal.Decimal(degree),rounding=decimal.ROUND_HALF_UP)

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    times, herald = (int(val) for val in line.split(SEPARATOR))

    if times > herald:
        print("Times has", times - herald, "more subscribers")
    elif herald > times:
        print("Herald has", herald - times, "more subscribers")
    else:
        print("Times and Herald have the same number of subscribers")