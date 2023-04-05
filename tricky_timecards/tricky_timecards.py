import sys
import decimal

def better_round(user_in, degree: str = "1.0"):
    '''Round Half Up'''
    return decimal.Decimal(user_in).quantize(decimal.Decimal(degree),rounding=decimal.ROUND_HALF_UP)

SEPARATOR = ","

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    timecard = []
    for val in line.split(SEPARATOR):
        timecard.append(val)

    employee = timecard[0]
    timecard.pop(0)

    totalHours = 0
    totalMinutes = 0

    for index, value in enumerate(timecard):
        hours, minutes = value.split(":")

        totalHours += int(hours)
        totalMinutes += int(minutes)

    while totalMinutes >= 60:
        totalHours += 1
        totalMinutes -= 60

    if totalMinutes == 0:
        if totalHours == 1:
            print(employee+"="+str(totalHours), "hour")
        else:
            print(employee+"="+str(totalHours), "hours")
    else:
        if totalHours == 1:
            if totalMinutes == 1:
                print(employee+"="+str(totalHours), "hour", str(totalMinutes), "minute")
            else:
                print(employee+"="+str(totalHours), "hour", str(totalMinutes), "minutes")
        else:
            if totalMinutes == 1:
                print(employee+"="+str(totalHours), "hours", str(totalMinutes), "minute")
            else:
                print(employee+"="+str(totalHours), "hours", str(totalMinutes), "minutes")