# Day 24: Blizzard Basin

from _getinput import *

def getblizzard(input, blizz = [], moves = []):

    dirs = {'>': (1,0), '<': (-1,0), 'v': (0,1), '^': (0,-1)}

    for y, line in enumerate(input):
        for x, char in enumerate(line):
            
            if char == '.':
                if y == 0: start = (x,y)
                if y == len(input)-1: end = (x,y)

            if char in dirs: 
                moves.append(dirs[char])
                blizz.append((x,y))

    blizzard = [blizz, moves]
    board = {'s': start, 'e': end, 
             'x': (1,len(input[0])-2), 
             'y': (1, len(input)-2)}

    return blizzard, board

def moveblizzard(blizzard, board, time, blizzmemory):

    if time in blizzmemory: 
        return blizzmemory[time]

    minx, maxx = board['x']
    miny, maxy = board['y']

    blizz, moves = blizzard

    for i in range(len(blizz)):
        x, y = blizz[i]
        dx, dy = moves[i]

        x += dx; y += dy

        if x == minx-1: x = maxx
        if x == maxx+1: x = minx
        if y == miny-1: y = maxy
        if y == maxy+1: y = miny

        blizz[i] = (x,y)

    blizzard = [blizz, moves]
    blizzmemory[time] = blizzard

    return blizzard

def nextsteps(me, blizzard, board):
    
    start = board['s']; end = board['e']
    minx, maxx = board['x']
    miny, maxy = board['y']

    x, y = me; blizz, _ = blizzard
    steps = []

    for step in [(x,y), (x,y-1), (x,y+1), (x-1,y), (x+1,y)]:
        notblizz = step not in set(blizz)
        notwall = (minx <= step[0] <= maxx) and (miny <= step[1] <= maxy)
        startorend = step in [start,end]

        if notblizz and (notwall or startorend):
            steps.append(step)

    return steps

def navigateblizzard(blizzard, blizzmemory, start, end, time):

    queue = [(start,time)]
    visited = set()

    while queue:
        me, time = queue.pop(0)

        if me == end: break

        if (me,time) not in visited:
            visited.add((me,time))

            blizzard = moveblizzard(blizzard, board, time, blizzmemory)
            steps = nextsteps(me, blizzard, board)

            for step in steps:
                queue.append((step,time+1))

    return time, blizzard

def savetheelves(blizzard, board):
    times = []
    blizzmemory = {}; time = 0
    moves = [('s','e'), ('e','s'), ('s','e')]

    for move in moves:
        s, e = move
        start = board[s]; end = board[e]
        time, blizzard = navigateblizzard(blizzard, blizzmemory, start, end, time)
        if e == 'e': times.append(time)

    return times
    
blizzard, board = getblizzard(getinput('24'))
end, endagain = savetheelves(blizzard, board)

print('Part 1:', end)
print('Part 2:', endagain)