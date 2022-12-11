# Day 1: Calorie Counting

from _preprocess import *

def elves(calories, maxcal = [], cals = 0):

    for cal in calories:
        
        if cal == '':
            maxcal.append(cals); cals = 0
        else:
            cals+=int(cal)

    maxcal.sort(reverse=True)

    print('Part 1:', maxcal[0])
    print('Part 2:', sum(maxcal[:3]))

calories = preprocess('01')
elves(calories)