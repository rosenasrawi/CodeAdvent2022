# Day 13: Distress Signal

from _preprocess import *
import json, itertools

def getpacks(packets, packs = []):

    for pack in packets:
        if len(pack) > 0: 
            packs.append(json.loads(pack))

    return packs

def leftvsright(l, r, decision = 0):

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
            decision = leftvsright(c[0],c[1])
            if decision != 0: break

        if decision == 0:
            if len(l) < len(r): decision = 1
            if len(r) < len(l): decision = -1

    return decision

def pairsinorder(packs, order = []):

    for i in range(0,len(packs),2):
        left = packs[i]; right = packs[i+1]
        decision = leftvsright(left,right)
        order.append(decision)

    order = [i+1 for i,o in enumerate(order) if o == 1]

    return (sum(order))

def orderpacks(packs, divider = [[[2]], [[6]]], index = []):

    packs += divider

    for i,p in enumerate(packs):

        others = packs.copy(); others.pop(i); pos = []

        for o in others:
            decision = leftvsright(p,o)

            if decision == 1: pos.append(False)
            else: pos.append(True)    

        index.append(sum(pos)+1)

    return index[-2] * index[-1]

packs = getpacks(preprocess('13')) 

print('Part 1:', pairsinorder(packs))
print('Part 2:', orderpacks(packs))