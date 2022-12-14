# Day 14: Regolith Reservoir

from _getinput import *
import re

def findrock(cave, depth = 0):

    rock = set()
    
    for path in cave:

        for i, coor in enumerate(path):
            rock.add(coor)

            if i < len(path)-1: 
                next = path[i+1]
                xran = [coor[0], next[0]]; xval = []
                yran = [coor[1], next[1]]; yval = []

                if abs(xran[0]-xran[1])>1:
                    xval = list(range(min(xran),max(xran)))
                    for x in xval: rock.add((x,coor[1]))

                if abs(yran[0]-yran[1])>1:
                    yval = list(range(min(yran),max(yran)))
                    for y in yval: rock.add((coor[0],y))

    depth = max([coor[1] for coor in rock])

    return rock, depth

def sandfall(rock, sand, depth, floor = 0):

    full = False; grain = [500,0]

    while True:

        if floor > 0 and (500,1) in rock and (501,1) in rock and (499,1) in rock:
            rock.add((500,0))
            sand.add((500,0))
            full = True; break
        elif floor == 0 and grain[1] > depth:
            full = True; break

        below = (grain[0],grain[1]+1) not in rock
        left = (grain[0]-1,grain[1]+1) not in rock
        right = (grain[0]+1,grain[1]+1) not in rock

        if below: 
            grain[1] += 1
        elif left and not below:
            grain[0] -= 1; grain[1] += 1
        elif right and not (below and left):
            grain[0] += 1; grain[1] += 1
        else:
            rock.add(tuple(grain))
            sand.add(tuple(grain))
            break

        if floor > 0 and grain[1]+1 == floor:
            rock.add(tuple(grain))
            sand.add(tuple(grain))
            break

    return full, sand

def fillcave(cave, abyss = True):

    sand = set(); full = False
    rock, depth = findrock(cave)

    if abyss: floor = 0
    else: floor = depth + 2

    while not full:
        full, sand = sandfall(rock, sand, depth, floor)

    return len(sand)

cave = [[tuple(map(int, re.split(',', coor))) 
                for coor in list(re.split('->', path))] 
                            for path in getinput('14')]

print('Part 1:', fillcave(cave))
print('Part 2:', fillcave(cave, abyss = False))