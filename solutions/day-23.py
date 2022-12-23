# Day 23: Unstable Diffusion

from _getinput import *
from collections import Counter

def findelves(input, elves = []):

    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char == '#':
                elf = (x,y)
                elves.append(elf)

    return elves

def getorder():
    
    return [('N','NE','NW'), ('S','SE','SW'), ('W','NW','SW'), ('E','NE','SE')]

def adjacent(x,y):

    adj = {'N': (x,y-1), 'S': (x,y+1), 
           'W': (x-1,y), 'E': (x+1,y),
           'NW': (x-1,y-1), 'NE': (x+1,y-1), 
           'SW': (x-1,y+1), 'SE': (x+1,y+1)}

    return adj

def elfupdate(elves, order):

    moves = []
    newelves = []

    elfset = set(elves)

    for elf in elves:
        x,y = elf
        adj = adjacent(x,y)
        dirs = adj.values()
        free = [d not in elfset for d in dirs]
        # free = [4,4]
        if sum(free) == 8:
            moves.append(elf)

        else:
            movetry = None

            for dir in order:

                pos = [adj[d] for d in dir]
                free = [p not in elfset for p in pos]

                if sum(free) == 3:
                    movetry = pos[0]
                    break
    
            if movetry == None:
                moves.append(elf)
            else: moves.append(movetry)

    movecounts = Counter(moves)

    for i in range(len(moves)):

        move = moves[i]; elf = elves[i]

        if movecounts[move] == 1:
            newelves.append(move)
        else: newelves.append(elf)

    elves = newelves
    order.append(order.pop(0))

    return elves, order

def ontrack(elves, empty = 0):

    order = getorder()
    for i in range(10):
        elves, order = elfupdate(elves,order)

    x = [elf[0] for elf in elves]
    y = [elf[1] for elf in elves]

    minx = min(x); maxx = max(x)
    miny = min(y); maxy = max(y)

    for x in range(minx,maxx+1):
        for y in range(miny,maxy+1):
            if (x,y) not in elves: empty += 1

    return empty

def elfspread(elves):

    order = getorder()
    round = 0; spread = False
    
    while not spread:
        oldelves = elves.copy()
        elves, order = elfupdate(elves,order)
        round += 1

        if elves == oldelves:
            spread = True
    
    return round

elves = findelves(getinput('23'))

print('Part 1:', ontrack(elves))
print('Part 2:', elfspread(elves))