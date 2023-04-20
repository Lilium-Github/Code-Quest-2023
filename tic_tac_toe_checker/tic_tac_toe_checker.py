'''System Module'''
import sys

def check_win(line, player):
    #checking diagonals
    if line[0] == player and line[0] == line[4] and line[0] == line[8]:
        return True
    if line[2] == player and line[2] == line[4] and line[2] == line[6]:
        return True
    
    #checking rows
    if line[0] == player and line[0] == line[1] and line[0] == line[2]:
        return True
    if line[3] == player and line[3] == line[4] and line[3] == line[5]:
        return True
    if line[6] == player and line[6] == line[7] and line[6] == line[8]:
        return True
    
    #checking columns
    if line[0] == player and line[0] == line[3] and line[0] == line[6]:
        return True
    if line[1] == player and line[1] == line[4] and line[1] == line[7]:
        return True
    if line[2] == player and line[2] == line[5] and line[2] == line[8]:
        return True
    
    return False
    

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    if check_win(line, "X"):
        print(line, "= X WINS")
    elif check_win(line, "O"):
        print(line, "= O WINS")
    else:
        print(line, "= TIE")
    