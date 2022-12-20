# Day 20: Grove Positioning System 

from _getinput import *

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

    return mixed, index, imax

def getgrove(mixed, imax):

    i0 = mixed.index(0)
    coor = [(i0 + n) % (imax + 1) for n in [1000,2000,3000]]

    grove = sum(mixed[c] for c in coor)

    return grove

def positioning(numbers, nmix = 1, decrypt = False, key = 811589153):

    mixed = numbers.copy()
    index = list(range(len(mixed)))
    imax = index[-1]; imin = -(imax+1)

    if decrypt:
        mixed = [num * key for num in mixed]

    for i in range(nmix):
        mixed, index, imax = mixing(mixed, index, imax, imin)

    return getgrove(mixed, imax)

numbers = list(map(int, getinput('20')))

print('Part 1:', positioning(numbers))
print('Part 2:', positioning(numbers, nmix = 10, decrypt = True))