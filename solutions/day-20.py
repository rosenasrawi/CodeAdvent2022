# Day 20: Grove Positioning System 

from _getinput import *
from collections import deque

def mixing(mixed, index, imax, imin):

    for i in range(len(mixed)):
        imove = index.index(i)
        move = mixed[imove]
        inext = imove+move

        if move != 0:

            if inext > imax: 
                inext %= imax
            if inext < imin: 
                inext %= -imax
            if inext == 0: 
                inext = imax

            n = mixed.pop(imove)
            id = index.pop(imove)

            mixed.insert(inext, n)
            index.insert(inext, id)

    return mixed, index

def mixing_rotate(mixed, index):

    for i in range(len(numbers)):
        imove = index.index(i)
        move = mixed[imove]

        del mixed[imove]
        del index[imove]

        mixed.rotate(-move)
        index.rotate(-move)

        mixed.insert(imove, move)
        index.insert(imove, i)

    return mixed, index

def getgrove(mixed):

    i0 = mixed.index(0)
    coor = [(i0 + n) % len(mixed) for n in [1000,2000,3000]]

    grove = sum(mixed[c] for c in coor)

    return grove

def position(numbers, nmix = 1, decrypt = False, key = 811589153):

    mixed = numbers.copy()
    index = list(range(len(mixed)))
    imax = index[-1]; imin = -(imax+1)

    if decrypt:
        mixed = [num * key for num in mixed]

    for i in range(nmix):
        mixed, index = mixing(mixed, index, imax, imin)

    return getgrove(mixed)

def position_rotate(numbers, nmix = 1, decrypt = False, key = 811589153):

    mixed = deque([num for num in numbers])
    index = deque(list(range(len(numbers))))

    if decrypt:
        mixed = [num * key for num in mixed]
        mixed = deque([num for num in mixed])

    for i in range(nmix):
        mixed, index = mixing_rotate(mixed, index)

    return getgrove(mixed)

numbers = list(map(int, getinput('20')))

import time

t1=time.time()
print('Part 1:', position(numbers))
print('Part 2:', position(numbers, nmix = 10, decrypt = True))
t2=time.time()
print('mod', t2-t1)

t1=time.time()
print('Part 1:', position_rotate(numbers))
print('Part 2:', position_rotate(numbers, nmix = 10, decrypt = True))
t2=time.time()
print('rot', t2-t1)

