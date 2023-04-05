import sys
import decimal

def better_round(user_in, degree: str = "1.0"):
    '''Round Half Up'''
    return decimal.Decimal(user_in).quantize(decimal.Decimal(degree),rounding=decimal.ROUND_HALF_UP)

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    num1, num2, num3 = (int(val) for val in line.split(SEPARATOR))

    if num1 + num2 == num3:
        print("Addition")
    elif num1 - num2 == num3:
        print("Subtraction")
    elif num1 * num2 == num3:
        print("Multiplication")
    elif num1 // num2 == num3:
        print("Division")
    elif num1 % num2 == num3:
        print("Modulo")