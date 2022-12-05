from _preprocess import *
import re

def splitdata(crates):

    stacks = {i: [] for i in list(range(1,10))}
    icol = [crates[8].index(i) for i in list(map(str,list(range(1,10))))]

    for i, c in enumerate(icol):
        for r in reversed(range(8)):
            if crates[r][c].isalpha():
                stacks[i+1].append(crates[r][c])

    rules = crates[10:]

    return stacks, rules

def movecrates(crates, rev = True):
    
    stacks, rules = splitdata(crates)
    
    for rule in rules:
        rule = list(map(int,re.findall(r'\d+', rule)))
        q = rule[0]; f = rule[1]; t = rule[2]
        
        move = stacks[f][-q:]
        if rev: move.reverse()
        stacks[t] += move
        for i in range(q): stacks[f].pop()

    top = ''
    for i in list(range(1,10)): 
        top += stacks[i][-1]

    return(top)

crates = preprocess('05')

print('Part 1:', movecrates(crates))
print('Part 2:', movecrates(crates, rev = False))