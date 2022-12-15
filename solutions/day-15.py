# Day 15: Beacon Exclusion Zone

from _getinput import *
import re, itertools

def manhattan(input, signal = []):

    for sig in input:
        sig = list(map(int,re.findall(r'-?\d+', sig)))
        sens, beac = sig[:2], sig[2:]
        dist = sum([abs(sens[i]-beac[i]) for i in range(2)])
        signal.append([sens,beac,dist])

    return signal

def findempty(signal, target, empty = []):

    for sig in signal:
        sx,sy = sig[0]; dist = sig[2]

        if sy-dist <= target <= sy+dist:
            xran = dist - abs(sy-target)
            empty.append([sx - xran, sx + xran])

    return empty        

def nobeacon(empty, target, tbeac = set()):
    empty = list(itertools.chain(*empty))
    nobeac = len(list(range(min(empty),max(empty)+1)))
    
    for sig in signal:
        beac = sig[1]
        if beac[1] == target and min(empty) <= beac[0] <= max(empty):
            tbeac.add(tuple(beac))

    return nobeac - len(tbeac)

def checkrange(empty, x, y):
    y+=1; empty.sort(); xrange = empty.pop(0)

    while empty:
        new = empty.pop(0)

        if new[0] > xrange[1]+1:
            x = xrange[1] + 1; break
        if new[1] > xrange[1]:
            xrange[1] = new[1]

    return x, y

def elfdistress(signal, target):

    if type(target) is int:
        empty = findempty(signal, target)
        nobeac = nobeacon(empty, target)
        return nobeac

    elif type(target) is list:
        y = -1; x = -1

        for t in target:
            empty = findempty(signal, t)
            x, y = checkrange(empty, x, y)
            if x > -1: 
                return x*4000000+y; break

signal = manhattan(getinput('15'))

print('Part 1:', elfdistress(signal, 2000000))
print('Part 2:', elfdistress(signal, list(range(4000000+1))))