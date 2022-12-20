# Day 20: Grove Positioning System 

from _getinput import *

def mixing(mixed, index, imax, imin):

    for i in range(len(mixed)):
        imove = index.index(i)
        move = mixed[imove]

        if move != 0:
            inext = imove+move

            if inext > imax:
                inext %= imax

            if inext < imin:
                inext %= -imax

            n = mixed.pop(imove)
            id = index.pop(imove)

            if inext == 0:
                mixed.append(n)
                index.append(id)
            else:
                mixed.insert(inext, n)
                index.insert(inext, id)

    return mixed, index, imax

def getgrove(mixed, imax):

    izero = mixed.index(0)
    coor = [(izero + n) % (imax + 1) for n in [1000,2000,3000]]

    grove = sum(mixed[c] for c in coor)

    return grove

def positioning(numbers, decrypt = False, key = 811589153):

    mixed = numbers.copy()
    index = list(range(len(mixed)))
    imax = index[-1]; imin = -(imax+1)

    if decrypt: 
        mixed = [num * key for num in mixed]
        
        for i in range(9):
            mixed, index, imax = mixing(mixed, index, imax, imin)

    mixed, index, imax = mixing(mixed, index, imax, imin)

    return getgrove(mixed, imax)

numbers = list(map(int, getinput('20')))

print('Part 1:', positioning(numbers))
print('Part 2:', positioning(numbers, decrypt = True))