# Day 14: Regolith Reservoir

from _getinput import *
import re

def makecave(rock, cave = set(), depth = 0):

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

def sandfall(cave, depth):

    full = False
    sand = [500,0]

    while True:

        below = (sand[0],sand[1]+1) not in cave
        left = (sand[0]-1,sand[1]+1) not in cave
        right = (sand[0]+1,sand[1]+1) not in cave

        if below: # I can go down!
            sand[1] += 1

        elif not below and left: # I can go left:
            sand[0] -= 1; sand[1] += 1

        elif not below and not left and right: # I can go right:
            sand[0] += 1; sand[1] += 1

        else: # Can't go anywhere
            print('end',sand)
            cave.add(tuple(sand))
            allsand.add(tuple(sand))
            break

        if sand[1] > depth: 
            full = True
            break

    return full

rock = getinput('14')
rock = [[tuple(map(int, re.split(',', coor))) for coor in list(re.split('->', path))] for path in rock]
cave, depth = makecave(rock)

sand = [500,0]
allsand = set()
full = False

while not full:
    full = sandfall(cave, depth)

print(len(allsand))