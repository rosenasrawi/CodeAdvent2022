# Day 1: Calorie counting

import os

def preprocess(datafile):
    wd = os.getcwd()
    with open(wd + "/01/" + datafile, "r") as calorieFile:
        calories = calorieFile.readlines()
        calories = [i.rstrip('\n') for i in calories]

    return calories

calories = preprocess('input.txt')

maxcal = []; cals = 0

for cal in calories:

    if cal != '':
        cals+=int(cal)
    elif cal == '':
        maxcal.append(cals)
        cals = 0

maxcal.sort(reverse=True)

print('Part 1:', max(maxcal))
print('Part 2:', sum(maxcal[:3]))
