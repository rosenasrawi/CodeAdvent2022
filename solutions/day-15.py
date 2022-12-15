# Day 15: beac Exclusion Zone

from _getinput import *
import re
import itertools

def manhattan(sens,beac):
    dist = sum([abs(sens[i]-beac[i]) for i in range(2)])
    return dist


signal = getinput('ex')
signal = [list(map(int,re.findall(r'-?\d+', sig))) for sig in signal]
distances = [manhattan(sig[:2],sig[2:]) for sig in signal]


target = 20
targets = list(range(target+1))
# targets = [10]

y = -1; x = -1

for target in targets:

    empty = []

    for i, sig in enumerate(signal):
        sens = sig[:2]; beac = sig[2:]
        dist = distances[i]

        ymin = sens[1]-dist
        ymax = sens[1]+dist

        if ymin <= target <= ymax:
            xran = dist - abs(sens[1]-target)
            xmin = sens[0] - xran
            xmax = sens[0] + xran
            empty.append([xmin,xmax])

    if len(targets) != 1:  
        empty.sort()
        range = empty.pop(0)
        y+=1

        while empty:
            new = empty.pop(0)

            if new[0] > range[1]+1:
                x = range[1] + 1; break
            if new[1] > range[1]:
                range[1] = new[1]

        if x > -1: break

    else:
        empty = list(itertools.chain(*empty))
        nobeac = len(list(range(min(empty),max(empty)+1)))
        beacattarg = set()

        for sig in signal:
            if sig[-1] == target and min(empty) <= sig[-2] <= max(empty):
                beacattarg.add((sig[-1],sig[-2]))
                
        print(len(beacattarg))
        nobeac -= len(beacattarg)

if len(targets) != 1:
    print(x*4000000+y)
else:
    print(nobeac)    




# empty = []

# for sig in signal:
#     sens = sig[:2]; beac = sig[2:]
#     dist = manhattan(sens,beac)

#     ymin = sens[1] - dist
#     ymax = sens[1] + dist

#     if ymin <= target <= ymax:
#         xran = dist - abs(sens[1]-target)
#         xmin = sens[0] - xran
#         xmax = sens[0] + xran
#         empty+=[xmin,xmax]

# nobeac = len(list(range(min(empty),max(empty)+1)))
# print(nobeac)

# beacattarg = set()

# for sig in signal:
#     if sig[-1] == target and min(empty) <= sig[-2] <= max(empty):
#         beacattarg.add((sig[-1],sig[-2]))

# print(beacattarg)

# nobeac -= len(beacattarg)
# print(nobeac)

