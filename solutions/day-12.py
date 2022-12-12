# Day 12: Hill Climbing Algorithm

from _preprocess import *
import string

def adjacent(next, rmax, cmax, adj = {'l':[], 'r':[], 'u':[], 'd':[]}):
    r, c = next

    adj['l'] = [r,c-1]; adj['r'] = [r,c+1]
    adj['u'] = [r-1,c]; adj['d'] = [r+1,c]

    if r == 0: adj.pop('u')
    if c == 0: adj.pop('l')
    if r == rmax-1: adj.pop('d')
    if c == cmax-1: adj.pop('r')
    
    return list(adj.values())

def step(l1, l2, letters = list(string.ascii_lowercase)):
    if l1 == 'S': l1 = 'a'
    if l2 == 'E': l2 = 'z'

    if letters.index(l2) - letters.index(l1) < 2:
        return True
    else: return False

map = preprocess('12')

for i, r in enumerate(map):
    if 'S' in r: start = [i,r.index('S')]
    if 'E' in r: end = [i, r.index('E')]


visited = []
queue = [start]
dist = []; distances = []

for c in range(len(map[0])):
    dist.append(0)
for r in range(len(map)):
    distances.append(dist.copy())

while queue:  
    next = queue.pop(0)
    l1 = map[next[0]][next[1]]

    if l1 == 'E': 
        visited.append(i); break

    if next not in visited:
        visited.append(next)

    adj = adjacent(next,len(map),len(map[0]))

    olddist = distances[next[0]][next[1]]

    for i in adj:

        l2 = map[i[0]][i[1]]

        if i not in visited:
            if step(l1,l2):
                distances[i[0]][i[1]] = olddist + 1
                
                # for d in distances: print(d)

                visited.append(i)
                queue.append(i)

print(distances[end[0]][end[1]])





