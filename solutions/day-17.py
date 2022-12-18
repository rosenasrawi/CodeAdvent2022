# Day 17: Pyroclastic Flow

from _getinput import *

def tetrisdata(input):

    shapes = {'-': [(2,0), (3,0), (4,0), (5,0)], 
              '+': [(2,1), (3,0), (3,1), (3,2), (4,1)], 
              'L': [(2,0), (3,0), (4,0), (4,1), (4,2)], 
              '|': [(2,0), (2,1), (2,2), (2,3)],
              'o': [(2,0), (3,0), (2,1), (3,1)]}

    order = ['-','+','L','|','o']
    ishapes = list(range(len(order)))

    moves = list(map(str,input))
    imoves = list(range(len(moves)))

    return shapes, order, ishapes, moves, imoves

def tetris(shape, moves, rockpos, height):
    
    rest = False
    
    while not rest:

        imove = imoves.pop(0); imoves.append(imove)
        move = moves[imove]
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

        dropped = [c.copy() for c in shape]
        for c in dropped: c[1] -= 1
        dropped = [tuple(c) for c in dropped]

        isrock = any([c in rockpos for c in dropped])
        isfloor = any([c[1] < 0 for c in dropped])

        if isrock or isfloor:
            for c in shape:
                rockpos.add(tuple(c))
                if c[1]+1 > height: height = c[1]+1
            rest = True
            
        else:
            for c in shape: c[1] -= 1

    return rockpos, height, moves

def buildtower(shapes, order, ishapes, moves, imoves):

    height = 0; rockpos = set()
    keys = []; states = []

    for i in range(int(1e12)):

        if i == 2022:
            print("Part 1:", height)

        key = (ishapes[0], imoves[0])
        state = (i, height)

        threeocc = keys.count(key) == 3
        
        if threeocc:
            cycles = [i for i, k in enumerate(keys) if k == key]
            evenlyspaced = cycles[1]-cycles[0] == cycles[2] - cycles[1]

            if evenlyspaced:
                ibeg, hbeg = states[cycles[1]]
                icycle, hcycle = states[cycles[2]]

                icycle, hcycle = icycle-ibeg, hcycle-hbeg

                div, mod = divmod(1e12-ibeg, icycle)
                div, mod = int(div), int(mod)

                if mod > 0:
                    imod = ibeg + mod
                    irest, hrest = states[imod]
                    total = hcycle*div + hrest
                else: 
                    total = hcycle*div + hbeg
                print("Part 2:", total)
                break

        else:
            states.append(state)
            keys.append(key)

        ishape = ishapes.pop(0); ishapes.append(ishape)
        shape = order[ishape]
        shape = [list(c) for c in shapes[shape]]

        for c in shape: c[1] += height + 3

        rockpos, height, moves = tetris(shape, moves, rockpos, height)

shapes, order, ishapes, moves, imoves = tetrisdata(getinput('17'))
buildtower(shapes, order, ishapes, moves, imoves)