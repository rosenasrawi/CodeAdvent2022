# Day 18: Boiling Boulders

from _getinput import *
import re

def neighbours(a, b):

    adj = sum([abs(a[i]-b[i]) for i in range(3)]) == 1

    return adj

def getsurface(points, sides = 6):

    drops = [points.pop(0)]

    while points:

        b = points.pop(0); nadj = []

        for a in drops:
            adj = neighbours(a,b)
            nadj.append(adj)

        sides += 6 - (2 * sum(nadj))

        drops.append(b)

    return sides, drops

def findair(lava, air = {}):
    
    x = [a[0] for a in lava]
    y = [a[1] for a in lava]
    z = [a[2] for a in lava]

    minx, maxx = min(x), max(x)
    miny, maxy = min(y), max(y)
    minz, maxz = min(z), max(z)

    for x in range(minx-1, maxx+1):
        for y in range(miny-1, maxy+1):
            for z in range(minz-1, maxz+1):

                if [x,y,z] not in lava:
                    air[(x,y,z)] = False

    return air, (minx,miny,minz)

def findtrapped(air, start, queue = []):

    queue.append(start)

    while queue:
        next = queue.pop(0)
        air[next] = True

        x,y,z = next
        adjacent = [(x-1,y,z), (x+1,y,z),
                    (x,y-1,z), (x,y+1,z),
                    (x,y,z-1), (x,y,z+1)]

        for a in adjacent:
            if a in air and air[a] == False and a not in queue:
                queue.append(a)

    trapped = [list(a) for a in air if air[a] == False]

    return trapped

def lavasurface(drops, exterior = False):
    
    drops = [list(map(int, re.findall(r'\d+', drop))) for drop in drops]

    surfacelava, lava = getsurface(drops)

    if exterior:

        air, start = findair(lava)
        trapped = findtrapped(air,start)

        surfacetrapped, _ = getsurface(trapped)
        surfacelava -= surfacetrapped

    return surfacelava

drops = getinput('18')

print('Part 1:', lavasurface(drops))
print('Part 2:', lavasurface(drops, exterior=True))