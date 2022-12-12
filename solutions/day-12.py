# Day 12: Hill Climbing Algorithm

from _preprocess import *
import string

def neighbour(next, rmax, cmax, adj = {'l':[], 'r':[], 'u':[], 'd':[]}):
    r, c = next

    adj['l'] = [r,c-1]; adj['r'] = [r,c+1]
    adj['u'] = [r-1,c]; adj['d'] = [r+1,c]

    if r == 0: adj.pop('u')
    if c == 0: adj.pop('l')
    if r == rmax-1: adj.pop('d')
    if c == cmax-1: adj.pop('r')
    
    return list(adj.values())

def makestep(l1, l2, reverse = False):
    
    letters = list(string.ascii_lowercase)
    if reverse: letters.reverse()

    if l1 == 'S': l1 = 'a'
    if l1 == 'E': l1 = 'z'
    if l2 == 'E': l2 = 'z'

    if letters.index(l2) - letters.index(l1) < 2:
        return True
    else: return False

def findpath(map, s, e, reverse = False):

    for i, r in enumerate(map):
        if s in r: start = [i,r.index(s)]

    visited = []; queue = [start]
    distances = []; dist = []
    for i in range(len(map[0])): dist.append(0)
    for i in range(len(map)): distances.append(dist.copy())

    while queue:  

        start = queue.pop(0)
        l1 = map[start[0]][start[1]]

        if l1 == e: visited.append(start); break
        if start not in visited: visited.append(start)

        adj = neighbour(start,len(map),len(map[0]))
        olddist = distances[start[0]][start[1]]

        for next in adj:
            l2 = map[next[0]][next[1]]

            if next not in visited:
                if makestep(l1,l2,reverse):
                    distances[next[0]][next[1]] = olddist + 1
                    visited.append(next)
                    queue.append(next)

    end = visited[-1]

    return distances[end[0]][end[1]]

map = preprocess('12')

print('Part 1:', findpath(map, s = 'S', e = 'E'))
print('Part 2:', findpath(map, s = 'E', e = 'a', reverse = True))