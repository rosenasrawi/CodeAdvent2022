# Day 9: Rope Bridge

from _preprocess import *
import numpy as np

def follow(head, tail):

    if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
        tail[0] += np.sign(head[0]-tail[0])
        tail[1] += np.sign(head[1]-tail[1])
        
    return tail

def ropebridge(moves, knots):
    
    visited = []
    rope = [[0,0] for i in range(knots)]

    for move in moves:

        dir, step = move.split()
        
        for s in range(int(step)):

            if dir == 'R': rope[0][0] += 1
            elif dir == 'L': rope[0][0] -= 1
            elif dir == 'U': rope[0][1] += 1
            elif dir == 'D': rope[0][1] -= 1

            for i in range(len(rope)-1):

                head = rope[i].copy(); tail = rope[i+1].copy()
                tail = follow(head,tail)
                rope[i] = head.copy(); rope[i+1] = tail.copy()     
            
            if tail not in visited: visited.append(tail.copy())

    return len(visited)

moves = preprocess('09')
print('Part 1:', ropebridge(moves,2))
print('Part 2:', ropebridge(moves,10))
