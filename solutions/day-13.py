# Day 13: Distress Signal

from _preprocess import *
from functools import cmp_to_key
import json

def getpacks(packets, packs = []):

    for pack in packets:

        if len(pack) > 0: 
            packs.append(json.loads(pack))

    return packs

def packorder(l, r, decision = 0):

    lint = type(l) is not list
    rint = type(r) is not list

    if lint and rint:
        if int(l) > int(r): decision = -1
        elif int(l) < int(r): decision = 1

    if (lint and not rint) or (rint and not lint):
        if lint: l = [l]; lint = False
        if rint: r = [r]; rint = False

    if not lint and not rint:
        comb = list(zip(l,r))

        for c in comb:
            decision = packorder(c[0],c[1])
            if decision != 0: break

        if decision == 0:
            if len(l) < len(r): decision = 1
            if len(l) > len(r): decision = -1

    return decision

def sortpairs(packs, order = []):

    for i in range(0,len(packs),2):
        left, right = packs[i:i+2]
        decision = packorder(left,right)
        order.append(decision)

    order = [i+1 for i,o in enumerate(order) if o == 1]

    return sum(order)

def sortpacks(packs, divider = [[[2]], [[6]]]):

    packs += divider
    packs.sort(key = cmp_to_key(packorder), reverse = True)
    decoderkey = [packs.index(i)+1 for i in divider]

    return decoderkey[0] * decoderkey[1]

packs = getpacks(preprocess('13'))

print('Part 1:', sortpairs(packs))
print('Part 2:', sortpacks(packs))