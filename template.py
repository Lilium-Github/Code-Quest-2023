'''System Module'''
import sys
import decimal

def better_round(user_in, degree: str = "1.0"):
    '''Round Half Up'''
    return decimal.Decimal(user_in).quantize(decimal.Decimal(degree),rounding=decimal.ROUND_HALF_UP)

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    val1, val2 = (float(val) for val in line.split(SEPARATOR))
    