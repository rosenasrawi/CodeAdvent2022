# Day 23: Unstable Diffusion

from _getinput import *

def findelves(input, elves = []):

    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char == '#':
                elf = (x,y)
                elves.append(elf)

    return elves

def adjacent(x,y):

    adj = {'N': (x,y-1), 'S': (x,y+1), 
           'W': (x-1,y), 'E': (x+1,y),
           'NW': (x-1,y-1), 'NE': (x+1,y-1), 
           'SW': (x-1,y+1), 'SE': (x+1,y+1)}

    return adj

def elfupdate(elves, order):

    moves = []
    newelves = []

    for elf in elves:
        x,y = elf
        adj = adjacent(x,y)
        dirs = adj.values()
        free = [d not in elves for d in dirs]

        if sum(free) == 8:
            moves.append(elf)

        else:
            movetry = None

            for dir in order:

                pos = [adj[d] for d in dir]
                free = [p not in elves for p in pos]

                if sum(free) == 3:
                    movetry = pos[0]
                    break
    
            if movetry == None:
                moves.append(elf)
            else: moves.append(movetry)
    
    for i in range(len(moves)):

        move = moves[i]; elf = elves[i]

        if moves.count(move) == 1:
            newelves.append(move)
        else: newelves.append(elf)

    elves = newelves
    order.append(order.pop(0))

    return elves, order

def elfspread(elves, order, empty = 0):

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

import time

t1 = time.time()

input = getinput('23')

elves = findelves(input)
order = [('N','NE','NW'), ('S','SE','SW'), ('W','NW','SW'), ('E','NE','SE')]

empty = elfspread(elves,order)

print(empty)

t2 = time.time()
print(t2-t1)
