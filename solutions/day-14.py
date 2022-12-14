# Day 14: Regolith Reservoir

from _getinput import *
import re

def makecave(rock, depth = 0):

    cave = set()
    
    for path in rock:

        for i, coor in enumerate(path):
            cave.add(coor)

            if i < len(path)-1: 
                next = path[i+1]
                
                xval = []; yval = []
                xc = coor[0]; xn = next[0]
                yc = coor[1]; yn = next[1]

                if abs(xc-xn)>1:
                    if xc > xn: xval = list(range(xc-1,xn,-1))
                    else: xval = list(range(xc+1,xn))

                if abs(yc-yn)>1:
                    if yc > yn: yval = list(range(yc-1,yn,-1))
                    else: yval = list(range(yc+1,yn))

                if xval: 
                    for x in xval: cave.add((x,coor[1]))
                if yval: 
                    for y in yval: cave.add((coor[0],y))

    for coor in cave:
        if coor[1] > depth: depth = coor[1]

    return cave, depth

def sandfall(cave, depth, allsand, floor = 0):

    full = False
    sand = [500,0]

    while True:

        if floor > 0 and (500,1) in cave and (501,1) in cave and (499,1) in cave:
            cave.add((500,0))
            allsand.add((500,0))
            full = True; break
        elif floor == 0 and sand[1] > depth:
            full = True; break

        below = (sand[0],sand[1]+1) not in cave
        left = (sand[0]-1,sand[1]+1) not in cave
        right = (sand[0]+1,sand[1]+1) not in cave

        if below: 
            sand[1] += 1
        elif left and not below:
            sand[0] -= 1; sand[1] += 1
        elif right and not (below and left):
            sand[0] += 1; sand[1] += 1
        else:
            cave.add(tuple(sand))
            allsand.add(tuple(sand))
            break

        if floor > 0 and sand[1]+1 == floor:
            cave.add(tuple(sand))
            allsand.add(tuple(sand))
            break

    return full, allsand

def fillcave(rock, abyss = True):

    allsand = set()
    cave, depth = makecave(rock)
    full = False

    if abyss: floor = 0
    else: floor = depth+2

    while not full:
        full, allsand = sandfall(cave, depth, allsand, floor)

    return len(allsand)

rock = [[tuple(map(int, re.split(',', coor))) for coor in list(re.split('->', path))] for path in getinput('14')]

print('Part 1:', fillcave(rock))
print('Part 2:', fillcave(rock, abyss = False))