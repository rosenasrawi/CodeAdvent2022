# Day 1: Calorie counting

import os

def preprocess(day):

    with open(os.getcwd() + day + '/input.txt', "r") as input:
        data = input.readlines()
        data = [i.rstrip('\n') for i in data]

    return data

def elves(calories):

    maxcal = []; cals = 0

    for cal in calories:

        if cal == '':
            maxcal.append(cals); cals = 0
        else:
            cals+=int(cal)

    maxcal.sort(reverse=True)

    print('Part 1:', maxcal[0])
    print('Part 2:', sum(maxcal[:3]))

calories = preprocess('/01')
elves(calories)