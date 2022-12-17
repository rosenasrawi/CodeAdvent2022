# Day 17: Pyroclastic Flow

from _getinput import *

moves = list(map(str,getinput('17')))

shapes = {'-': [(2,0), (3,0), (4,0), (5,0)], 
          '+': [(2,1), (3,0), (3,1), (3,2), (4,1)], 
          'L': [(2,0), (3,0), (4,0), (4,1), (4,2)], 
          '|': [(2,0), (2,1), (2,2), (2,3)],
          'o': [(2,0), (3,0), (2,1), (3,1)]}

order = ['-','+','L','|','o']

height = 0 # How high is the tower
rockpos = set() # Keep track of all the rocks positions

def tetris(shape, moves, rockpos, height):
    
    rest = False
    
    while not rest:

        move = moves.pop(0); moves.append(move)
        
        # Move left/right

        moved = [c.copy() for c in shape]

        if move == '>':
            for c in moved: c[0] += 1
            moved = [tuple(c) for c in moved]

            isrock = any([c in rockpos for c in moved])
            iswall = any([c[0] > 6 for c in moved])

            if not isrock and not iswall:
                for c in shape: c[0] += 1
    
        if move == '<':
            for c in moved: c[0] -= 1
            moved = [tuple(c) for c in moved]

            isrock = any([c in rockpos for c in moved])
            iswall = any([c[0] < 0 for c in moved])

            if not isrock and not iswall:
                for c in shape: c[0] -= 1

        # Drop one down
        dropped = [c.copy() for c in shape]
        for c in dropped: c[1] -= 1
        dropped = [tuple(c) for c in dropped]

        # Check if this dropped shape possible
        isrock = any([c in rockpos for c in dropped])
        isfloor = any([c[1] < 0 for c in dropped])

        if isrock or isfloor: # cannot drop
            for c in shape:
                rockpos.add(tuple(c)) # comes to rest
                if c[1]+1 > height: height = c[1]+1 # update height
            rest = True
            
        else: # can drop
            for c in shape: c[1] -= 1 # shape drops one down

    return rockpos, height, moves

for i in range(2022):
    shape = order.pop(0); order.append(shape)
    shape = [list(c) for c in shapes[shape]]

    for c in shape: c[1] += height + 3

    rockpos, height, moves = tetris(shape, moves, rockpos, height)

print(height, len(rockpos))
