# Day 7: No Space Left On Device

from _getinput import *

def filesystem(commands, dirs = {'/': 0}, curdir = ['/']):

    for c in commands:

        c = c.split(' ')

        if c[1] == 'cd':
            if c[2] == '..':
                dir = curdir.copy(); curdir.pop()
                dirs[''.join(curdir)] += dirs[''.join(dir)]
            elif c[2] != '/': 
                curdir.append(c[2])
        
        if c[0].isnumeric():
            dirs[''.join(curdir)] += int(c[0])

        if c[0] == 'dir':
            dirs[''.join(curdir + [c[1]])] = 0

    while len(curdir) != 1:
        dir = curdir.copy(); curdir.pop()
        dirs[''.join(curdir)] += dirs[''.join(dir)]

    return dirs

def freespace(dirs, sizes, memory = 70000000, space = 30000000):

    small = sum([dirs[i] for i in dirs if dirs[i] <= 100000])
    remove = [s for s in sizes if memory-dirs['/']+s >= space]

    return small, min(remove)

dirs = filesystem(getinput('07')); sizes = [dirs[i] for i in dirs]
small, large = freespace(dirs, sizes)

print('Part 1:', small)
print('Part 2:', large)