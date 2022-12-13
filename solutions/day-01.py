# Day 1: Calorie Counting

from _getinput import *

def elves(calories, maxcal = [], cals = 0):

    for cal in calories:
        
        if cal == '':
            maxcal.append(cals); cals = 0
        else:
            cals+=int(cal)

    maxcal.sort(reverse=True)

    return maxcal

maxcal = elves(getinput('01'))

print('Part 1:', maxcal[0])
print('Part 2:', sum(maxcal[:3]))