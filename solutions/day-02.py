# Day 2: ...

from _preprocess import *

rounds = preprocess('02')

total = {'other':0, 'self':0}

hands = {'A':1, 'X':1, 'B':2, 'Y':2, 'C':3, 'Z':3 }
draw = ['A X', 'B Y', 'C Z']
win = ['A Y', 'B Z', 'C X']

for r in rounds:

    total['other'] += hands[r[0]]
    total['self'] += hands[r[2]]

    if r in draw:
        total['other'] += 3
        total['self'] += 3
    elif r in win:
        total['self'] += 6
    else:
        total['other'] += 6

total = {'other':0, 'self':0}

draw = {'A':'X', 'B':'Y', 'C':'Z'}
win = {'A':'Y', 'B':'Z', 'C':'X'}
lose = {'A':'Z', 'B':'X', 'C':'Y'}

for r in rounds:
    total['other'] += hands[r[0]]

    if r[2] == 'X':
        hand = lose[r[0]]
        total['other'] += 6
    elif r[2] == 'Y':
        hand = draw[r[0]]
        total['other'] += 3
        total['self'] += 3
    elif r[2] == 'Z':
        hand = win[r[0]]
        total['self'] += 6

    total['self'] += hands[hand]

print(total)

rounds = preprocess('02')