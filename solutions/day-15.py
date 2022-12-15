# Day 15: beac Exclusion Zone

from _getinput import *
import re

signal = getinput('ex')
signal = [list(map(int,re.findall(r'\d+', sig))) for sig in signal]
print(signal)

target = 10 #2000000

def manhattan(sens,beac):
    dist = sum([abs(sens[i]-beac[i]) for i in range(2)])
    return dist

empty = []

for sig in signal:
    sens = sig[:2]; beac = sig[2:]
    dist = manhattan(sens,beac)

    ymin = sens[1] - dist
    ymax = sens[1] + dist

    if ymin <= target <= ymax:
        xran = dist - abs(sens[1]-target)
        xmin = sens[0] - xran
        xmax = sens[0] + xran
        empty+=[xmin,xmax]

nobeac = len(list(range(min(empty),max(empty)+1)))
print(nobeac)

beacattarg = set()

for sig in signal:
    if sig[-1] == target and min(empty) <= sig[-2] <= max(empty):
        beacattarg.add((sig[-1],sig[-2]))

print(beacattarg)

nobeac -= len(beacattarg)
print(nobeac)


# Part 2:

for sig in signal:
    sens = sig[:2]; beac = sig[2:]
    dist = manhattan(sens,beac)
    print(sens,dist)
    # print(sens[0]-dist, sens[0], sens[0]+dist, 
    #       sens[1]-dist, sens[1], sens[1]+dist)