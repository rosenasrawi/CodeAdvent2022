# Day 1: Calorie counting

import os

def preprocess(datafile):
    wd = os.getcwd()
    with open(wd + "/01/" + datafile, "r") as calorieFile:
        calories = calorieFile.readlines()
        calories = [i.rstrip('\n') for i in calories]

    return calories

def elves(calories):

    maxcal = []; cals = 0

    for cal in calories:

        if cal != '':
            cals+=int(cal)
        elif cal == '':
            maxcal.append(cals)
            cals = 0

    maxcal.sort(reverse=True)

    return max(maxcal), sum(maxcal[:3])

calories = preprocess('input.txt')
solution = elves(calories)

print('Part 1:', solution[0], ',', 'Part 2:', solution[1])