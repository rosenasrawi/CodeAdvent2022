# Day 22: Monkey Map

from _getinput import *
import re

def getdirections(input):

    positions = {}
    map, path = input[:-2], input[-1]

    path = re.split('(\d+)', path)
    path.pop(0); path.pop()

    for y, line in enumerate(map):
        for x, pos in enumerate(line):

            if pos == '.':
                if positions == {}:
                    loc = (x,y)
                positions[(x,y)] = True

            elif pos == '#':
                positions[(x,y)] = False

    turns = {(1,0)  : {'R': (0,1), 'L': (0,-1)},
             (-1,0) : {'R': (0,-1), 'L': (0,1)},
             (0,-1) : {'R': (1,0), 'L': (-1,0)},
             (0,1)  : {'R': (-1,0), 'L': (1,0)}}

    facings = {(1,0): 0, (0,1): 1, (-1,0): 2, (0,-1): 3}

    return path, loc, positions, turns, facings

def navigate(input, dx = 1, dy = 0, cube = False):

    path, loc, positions, turns, facings = getdirections(input)
    x, y = loc

    for step in path:

        if step.isnumeric():

            for i in range(int(step)):
                nx, ny = x+dx, y+dy
                state = positions.get((nx,ny))
                if cube: dir = None

                if state == None: # Wrap

                    if not cube:
                        nx, ny = x, y
                        wrapped = False
                        
                        while not wrapped:
                            nx -= dx; ny -= dy
                            state = positions.get((nx,ny))
                            
                            if state == None:
                                nx += dx; ny += dy
                                state = positions.get((nx,ny))
                                wrapped = True

                    if cube:
                        nx, ny, dir = transition(nx,ny,(dx,dy))
                        state = positions.get((nx,ny))

                if not state: # Reach wall
                    break

                if state: # Update position
                    x, y = nx, ny
                    if cube and dir != None:
                        dx, dy = dir

        else: dx, dy = turns[(dx,dy)][step]

    row = y+1; col = x+1; face = facings[(dx,dy)]

    return row * 1000 + col * 4 + face

def transition(x,y,dir):

    if  50 <= x < 100 and y == 150 and dir == (0,1): 
        nx = 49; ny = 150 + (x-50); dir = (-1,0)
    
    if x == 50 and 150 <= y < 200 and dir == (1,0):
        nx = 50 + (y-150); ny = 149; dir = (0,-1)

    if x == 100 and 50 <= y < 100 and dir == (1,0):
        nx = 50 + y; ny = 49; dir = (0,-1)
    
    if 100 <= x < 150 and y == 50 and dir == (0,1):
        nx = 99; ny = x - 50; dir = (-1,0)

    if x == 49 and 50 <= y < 100 and dir == (-1,0):
        nx = y-50; ny = 100; dir = (0,1)

    if 0 <= x < 50 and y == 99 and dir == (0,-1):
        nx = 50; ny = x + 50; dir = (1,0)

    if x == 150 and 0 <= y < 50 and dir == (1,0):
        nx = 99; ny = (49 - y) + 100; dir = (-1,0)

    if x == 100 and 100 <= y < 150 and dir == (1,0):
        nx = 149; ny = 49 - (y - 100); dir = (-1,0)

    if x == 49 and 0 <= y < 50 and  dir == (-1,0):
        nx = 0; ny = (49 - y) + 100; dir = (1,0)

    if x == -1 and 100 <= y < 150 and  dir == (-1,0):
        nx = 50; ny = 49 - (y - 100); dir = (1,0)

    if 100 <= x < 150 and y == -1 and dir == (0,-1):
        nx = x - 100; ny = 199; dir = (0,-1)

    if 0 <= x < 50 and y == 200 and dir == (0,1):
        nx = x + 100; ny = 0; dir = (0,1)

    if 50 <= x < 100 and y == -1 and dir == (0,-1):
        nx = 0; ny = 100 + x; dir = (1,0) 

    if x == -1 and 150 <= y < 200 and dir == (-1,0):
        nx = y - 100; ny = 0; dir = (0,1)

    return nx, ny, dir

input = getinput('22')

print('Part 1:', navigate(input))
print('Part 2:', navigate(input, cube = True))