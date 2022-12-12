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

def step(l1, l2, reverse = False, letters = list(string.ascii_lowercase)):
    if l1 == 'S': l1 = 'a'
    if l2 == 'E': l2 = 'z'
    if l1 == 'E': l1 = 'z'

    if reverse:
        if letters.index(l1) - letters.index(l2) < 2:
            return True
        else: return False   
    else:    
        if letters.index(l2) - letters.index(l1) < 2:
            return True
        else: return False

def findstart(map, reverse = False):

    for i, r in enumerate(map):
        if reverse:
            if 'E' in r: start = [i,r.index('E')]
        else:
            if 'S' in r: start = [i,r.index('S')]

    return start

def distmat(map, distances, dist = []):

    for i in range(len(map[0])): dist.append(0)
    for i in range(len(map)): distances.append(dist.copy())

    return distances

def findpath(map, reverse = False):

    start = findstart(map, reverse)
    visited = []; queue = [start]
    distances = distmat(map, distances = [])

    while queue:  
        start = queue.pop(0)
        l1 = map[start[0]][start[1]]

        if reverse:
            if l1 == 'a': 
                visited.append(start); break
        else:
            if l1 == 'E': 
                visited.append(start); break

        if start not in visited:
            visited.append(start)

        neighbours = adjacent(start,len(map),len(map[0]))
        olddist = distances[start[0]][start[1]]

        for next in neighbours:
            l2 = map[next[0]][next[1]]

            if next not in visited:
                if step(l1,l2,reverse):
                    distances[next[0]][next[1]] = olddist + 1
                    visited.append(next)
                    queue.append(next)

    end = visited[-1]

    return distances[end[0]][end[1]]

map = preprocess('12')

print('Part 1:', findpath(map))
print('Part 2:', findpath(map,reverse = True))