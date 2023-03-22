'''System Module'''
import sys
import decimal

def better_round(user_in, degree: str = "1.0"):
    '''Round Half Up'''
    return decimal.Decimal(user_in).quantize(decimal.Decimal(degree),rounding=decimal.ROUND_HALF_UP)

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    player = line.split(":")[0]
    atBats = line.split(":")[1].split(",")

    runs = 0

    while "BB" in atBats:
        atBats.remove("BB")

    if not atBats or atBats[0] == "":
        print(player + "=0.000")
    else:
        for index,val in enumerate(atBats):
            if val[0].isdecimal():
                runs += int(val[0])
            elif val == "HR":
                runs += 4

        slg = runs / len(atBats)

        slg = better_round(slg, degree="1.000")

        print(player + "=" + str(slg))
