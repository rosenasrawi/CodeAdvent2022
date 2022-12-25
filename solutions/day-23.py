# Day 23: Unstable Diffusion

from _getinput import *
from collections import Counter

def findelves(input, elves = []):

    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char == '#':
                elf = (x,y)
                elves.append(elf)

    order = [('N','NE','NW'), ('S','SE','SW'), ('W','NW','SW'), ('E','NE','SE')]

    return elves, order

def adjacent(x,y):

    adj = {'N': (x,y-1), 'S': (x,y+1), 
           'W': (x-1,y), 'E': (x+1,y),
           'NW': (x-1,y-1), 'NE': (x+1,y-1), 
           'SW': (x-1,y+1), 'SE': (x+1,y+1)}

    return adj

def elfupdate(elves, order):

    moves = elves.copy()
    elfset = set(elves)

    for i, elf in enumerate(elves):
        x,y = elf
        adj = adjacent(x,y); dirs = adj.values()
        free = [d not in elfset for d in dirs]

        if sum(free) < 8:
            movetry = None

            for dir in order:
                pos = [adj[d] for d in dir]
                free = [p not in elfset for p in pos]

                if sum(free) == 3:
                    movetry = pos[0]
                    break
    
            if movetry != None:
                moves[i] = movetry

    movecounts = Counter(moves)

    for i, move in enumerate(moves):

        if movecounts[move] == 1:
            elves[i] = move

    order.append(order.pop(0))

    return elves, order

def elfspread(elves, order):

    empty = 0; round = 0; spread = False
    
    while not spread:
        oldelves = elves.copy()
        elves, order = elfupdate(elves,order)
        round += 1

        if round == 10:
            x = [elf[0] for elf in elves]
            y = [elf[1] for elf in elves]

            minx = min(x); maxx = max(x)
            miny = min(y); maxy = max(y)

            for x in range(minx,maxx+1):
                for y in range(miny,maxy+1):
                    if (x,y) not in elves: empty += 1
                    
        if elves == oldelves:
            spread = True

    return empty, round

elves, order = findelves(getinput('23'))
empty, round = elfspread(elves, order)

print('Part 1:', empty)
print('Part 2:', round)