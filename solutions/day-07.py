# Day 7: No Space Left On Device

from _preprocess import *

def filesystem(commands, tree = {'/': 0}, curdir = ['/']):

    for c in commands:

        c = c.split(' ')

        if c[1] == 'cd':
            if c[2] == '/':
                curdir = ['/']
            elif c[2] == '..':
                curdir.pop()
            else: 
                curdir.append(c[2])
        
        if c[0].isnumeric():
            dir = []
            for val in curdir:
                dir.append(val)
                tree[''.join(dir)] += int(c[0])

        if c[0] == 'dir':
            dir = ''.join(curdir + [c[1]])
            if dir not in tree:
                tree[dir] = 0

    return tree

def freespace(tree, remove = [], space = 70000000):

    space -= tree['/']
    sizes = [tree[i] for i in tree]
    remove = [size for size in sizes if space+size >=30000000]

    small = sum([tree[i] for i in tree if tree[i] <= 100000])
    large = min(remove)

    return small,large

small, large = freespace(filesystem(preprocess('07')))
print('Part 1:', small); print('Part 2:', large)