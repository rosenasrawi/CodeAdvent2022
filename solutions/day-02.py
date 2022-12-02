# Day 2: Rock Paper Scissors

from _preprocess import *

def rockpapsci(rounds):

    total = {'Part 1':0, 'Part 2':0}
    hands = {'A':1, 'X':1, 'B':2, 'Y':2, 'C':3, 'Z':3 }

    # Part 1
    draw = ['A X', 'B Y', 'C Z']
    win = ['A Y', 'B Z', 'C X']

    for r in rounds:

        total['Part 1'] += hands[r[2]]

        if r in draw:
            total['Part 1'] += 3
        elif r in win:
            total['Part 1'] += 6

    # Part 2
    draw = {'A':'X', 'B':'Y', 'C':'Z'}
    win = {'A':'Y', 'B':'Z', 'C':'X'}
    lose = {'A':'Z', 'B':'X', 'C':'Y'}

    for r in rounds:

        if r[2] == 'X':
            hand = lose[r[0]]
        elif r[2] == 'Y':
            hand = draw[r[0]]
            total['Part 2'] += 3
        elif r[2] == 'Z':
            hand = win[r[0]]
            total['Part 2'] += 6

        total['Part 2'] += hands[hand]

    return total

rounds = preprocess('02')
print(rockpapsci(rounds))