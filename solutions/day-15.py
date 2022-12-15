# Day 15: beac Exclusion Zone

from _getinput import *
import re, itertools

def manhattan(sens,beac):
    return sum([abs(sens[i]-beac[i]) for i in range(2)])

def elfdistress(signal, distances, part):

    if part == 1:
        targets = [2000000]
        beacattarg = set()
    elif part == 2:
        targets = list(range(4000000+1))
        y = -1; x = -1

    for target in targets:

        empty = []

        for i, sig in enumerate(signal):
            sens = sig[:2]
            dist = distances[i]

            ymin = sens[1]-dist
            ymax = sens[1]+dist

            if ymin <= target <= ymax:
                xran = dist - abs(sens[1]-target)
                xmin = sens[0] - xran
                xmax = sens[0] + xran
                empty.append([xmin,xmax])

        if part == 1:  
            empty = list(itertools.chain(*empty))
            nobeac = len(list(range(min(empty),max(empty)+1)))
            
            for sig in signal:
                if sig[-1] == target and min(empty) <= sig[-2] <= max(empty):
                    beacattarg.add((sig[-1],sig[-2]))  

            nobeac -= len(beacattarg)

        elif part == 2:
            empty.sort()
            xrange = empty.pop(0)
            y+=1

            while empty:
                new = empty.pop(0)

                if new[0] > xrange[1]+1:
                    x = xrange[1] + 1; break
                if new[1] > xrange[1]:
                    xrange[1] = new[1]

            if x > -1: break

    if part == 1: return nobeac
    elif part == 2: return x*4000000+y

signal = getinput('15')
signal = [list(map(int,re.findall(r'-?\d+', sig))) for sig in signal]
distances = [manhattan(sig[:2],sig[2:]) for sig in signal]

print('Part 1:', elfdistress(signal, distances, 1))
print('Part 2:', elfdistress(signal, distances, 2))