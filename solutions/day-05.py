# Day 5: Supply Stacks

from _preprocess import *
import re

def getstacks(crates):

    for e, line in enumerate(crates):
        if len(line) < 1: break

    cols = re.findall(r'\d+', crates[e-1])
    icol = [crates[e-1].index(c) for c in cols]
    
    stacks = {int(c): [] for c in cols}
    moves = crates[e+1:]

    for i, c in enumerate(icol):
        for r in reversed(range(e-1)):
            if crates[r][c].isalpha():
                stacks[i+1].append(crates[r][c])

    return stacks, moves

def movecrates(crates, rev = True, top = ''):
    
    stacks, moves = getstacks(crates)
    
    for move in moves:
        move = list(map(int,re.findall(r'\d+', move)))
        qt = move[0]; fr = move[1]; to = move[2]
        
        substack = stacks[fr][-qt:]
        if rev: substack.reverse()

        stacks[to] += substack
        stacks[fr] = stacks[fr][:len(stacks[fr]) - qt]

    for t in range(len(stacks)):
        top += stacks[t+1][-1]

    return top

crates = preprocess('05')

print('Part 1:', movecrates(crates))
print('Part 2:', movecrates(crates, rev = False))