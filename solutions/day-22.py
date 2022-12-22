# Day 22: Monkeymap

from _getinput import *
import re

def getdirections(input, positions = {}):

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

def navigate(input, dx = 1, dy = 0):

    path, loc, positions, turns, facings = getdirections(input)

    x, y = loc

    for step in path:

        if step.isnumeric():

            for i in range(int(step)):
                nx, ny = x+dx, y+dy
                state = positions.get((nx,ny))

                if state == None: # Wrap

                    nx, ny = x, y
                    wrapped = False
                    
                    while not wrapped:
                        nx -= dx
                        ny -= dy

                        state = positions.get((nx,ny))
                        
                        if state == None:
                            nx += dx; ny += dy
                            state = positions.get((nx,ny))
                            wrapped = True

                if not state: # Reach wall
                    break

                if state: # Update position
                    x, y = nx, ny

        else:
            dx, dy = turns[(dx,dy)][step]

    row = y+1; col = x+1
    face = facings[(dx,dy)]
    answer = row * 1000 + col * 4 + face

    print(row, col, face)
    return answer

input = getinput('22')
print('Part 1:', navigate(input))

# Start part 2

def transition(x,y,dir):

    # 4 > 6 (A)
    if  99 < x < 200 and y == 300 and dir == (0,1): 
        nx = 99 
        ny = 300 + (x-100)
        dir = (-1,0)
    
    # 6 > 4 (A)
    if x == 100 and 299 < y < 400 and dir == (1,0):
        nx = 100 + (y-300)
        ny = 299
        dir = (0,-1)

    # 3 > 2 (D)
    if x == 200 and 99 < y < 200 and dir == (1,0):
        nx = 100 + y
        ny = 99
        dir = (0,-1)
    
    # 2 > 3 (D)
    if 199 < x < 300 and y == 100 and dir == (0,1):
        nx = 199
        ny = x - 100
        dir = (-1,0)

    return nx,ny,dir

print(transition(100,300,(0,1))) # test 4 > 6
print(transition(100,300,(1,0))) # test 6 > 4