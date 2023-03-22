import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    U = int(input())
    upper_lengths = [int(val) for val in input().split(SEPARATOR)]

    L = int(input())
    lower_lengths = [int(val) for val in input().split(SEPARATOR)]

    msg = input()

    #create uppercase messages
    upper_msgs = []
    curr_msg = str()
    msg_counter = 0

    for index, char in enumerate(msg):
        if char.isupper() or char == "-":
            if char == "-":
                curr_msg += " "
            else:
                curr_msg += char

            if len(curr_msg) == upper_lengths[msg_counter]:
                upper_msgs.append(curr_msg)
                curr_msg = str()
                msg_counter += 1

    #create lowercase messages
    lower_msgs = []
    curr_msg = str()
    msg_counter = 0

    for index, char in enumerate(msg):
        if char.islower() or char == "=":
            if char == "=":
                curr_msg += " "
            else:
                curr_msg += char

            if len(curr_msg) == lower_lengths[msg_counter]:
                lower_msgs.append(curr_msg)
                curr_msg = str()
                msg_counter += 1

    for index, string in enumerate(upper_msgs):
        print(string)

    print("")

    for index, string in enumerate(lower_msgs):
        print(string)

