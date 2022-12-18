# Day 17: Pyroclastic Flow

from _getinput import *

def tetris(shape, moves, rockpos, height):
    
    rest = False
    
    while not rest:

        imove = imoves.pop(0); imoves.append(imove)
        move = moves[imove]

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

    return rockpos, height, moves, imove, shape


moves = list(map(str,getinput('17')))

shapes = {'-': [(2,0), (3,0), (4,0), (5,0)], 
          '+': [(2,1), (3,0), (3,1), (3,2), (4,1)], 
          'L': [(2,0), (3,0), (4,0), (4,1), (4,2)], 
          '|': [(2,0), (2,1), (2,2), (2,3)],
          'o': [(2,0), (3,0), (2,1), (3,1)]}

order = ['-','+','L','|','o']

ishapes = list(range(len(order)))
imoves = list(range(len(moves)))

height = 0 # How high is the tower
rockpos = set() # Keep track of all the rocks in tower

states = {}; keys = []


for i in range(int(1e12)):

    state = (ishapes[0], imoves[0])

    if state in states:
        print("Cycle!")
        ibeg, hbeg = states[state]
        icycle, hcycle = i-ibeg, height-hbeg

        div, mod = divmod(1e12-ibeg, icycle)
        div, mod = int(div), int(mod)
        print(icycle, hcycle, ibeg, hbeg)

        if mod > 0:
            print("Rest cycle")
            imod = ibeg + mod-1
            key = keys[imod]
            irest, hrest = states[key]
            total = hcycle*div + hrest
            print(total)
        else: 
            print("No rest cycle")
            total = hcycle*div + hbeg
            print(total)

        break

    else: 
        states[state] = i, height
        keys.append(state)

    ishape = ishapes.pop(0); ishapes.append(ishape)
    shape = order[ishape]
    shape = [list(c) for c in shapes[shape]]

    for c in shape: c[1] += height + 3

    rockpos, height, moves, imove, shape = tetris(shape, moves, rockpos, height)