# Day 2: Rock Paper Scissors

from _getinput import *

def rockpapsci(rounds, total = [0,0], hands = {'X':1, 'Y':2, 'Z':3 }):

    draw = ['A X', 'B Y', 'C Z']
    win = ['A Y', 'B Z', 'C X']

    for r in rounds:

        if r in draw: 
            total[0] += 3
        elif r in win: 
            total[0] += 6

        total[0] += hands[r[2]]

    draw = {'A':'X', 'B':'Y', 'C':'Z'}
    win = {'A':'Y', 'B':'Z', 'C':'X'}
    lose = {'A':'Z', 'B':'X', 'C':'Y'}

    for r in rounds:

        if r[2] == 'X': 
            hand = lose[r[0]]
        elif r[2] == 'Y':
            hand = draw[r[0]]
            total[1] += 3
        elif r[2] == 'Z':
            hand = win[r[0]]
            total[1] += 6

        total[1] += hands[hand]

    return total

total = rockpapsci(getinput('02'))

print('Part 1:', total[0])
print('Part 2:', total[1])