# Day 7: No Space Left On Device

from _preprocess import *

def maketree(commands, tree = {'/R':0}, curdir = '/R'):

    for c in commands:

        c = c.split(' ')

        if c[1] == 'cd':
            if c[2] == '/':
                curdir = '/R'
            elif c[2] == '..':
                while curdir[-1] != '/':
                    curdir = curdir[:-1]
                curdir = curdir[:-1]    
            else: curdir += '/' + c[2]
        
        if c[0].isnumeric():
            dir = ''; curdir += '/'
            for i, val in enumerate(curdir):
                dir += val
                if i > 1 and dir[i] == '/':
                    tree[dir[:-1]] += int(c[0])
            curdir = curdir[:-1] 

        if c[0] == 'dir':
            d = curdir + '/' + c[1]
            if d not in tree:
                tree[d] = 0

    return tree

def freespace(tree, remove = [], space = 70000000):

    space -= tree['/R']

    for size in [tree[i] for i in tree]:
        if space + size >= 30000000:
            remove.append(size)

    return min(remove)

commands = preprocess('07')
tree = maketree(commands)

print('Part 1:', sum([tree[i] for i in tree if tree[i] <= 100000]))
print('Part 2:', freespace(tree))