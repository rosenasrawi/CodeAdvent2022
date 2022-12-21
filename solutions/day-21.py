# Day 21: Monkey Math

from _getinput import *
import re

def getmonkeys(input, monkeys = {}):

    for line in input:
        m, oper = re.split(': ', line)
        if oper.isnumeric():
            monkeys[m] = int(oper)
        else: monkeys[m] = oper

    return monkeys

def monkeymath(monkeys):

    while isinstance(monkeys['root'], str):
        
        for m in monkeys:
            yell = monkeys[m]

            if isinstance(yell, str):
                m1, op, m2 = re.split(' ', yell)

                n1 = monkeys[m1]
                n2 = monkeys[m2]

                if not isinstance(n1, str) and not isinstance(n2, str):

                    if op == '+': n = n1 + n2
                    if op == '-': n = n1 - n2
                    if op == '*': n = n1 * n2
                    if op == '/': n = n1 / n2

                    monkeys[m] = n

    return monkeys

def checksign(monkeys, rootl, rootr):

    newmonkeys = monkeys.copy()
    newmonkeys['humn'] = 0
    newmonkeys = monkeymath(newmonkeys)

    left = newmonkeys[rootl]
    right = newmonkeys[rootr]

    if left-right > 0: 
        return [0,1]
    elif left-right < 0:
        return [1,0]

def findhumn(monkeys, settled = False, hbounds = [0,int(5e14)]):

    root = monkeys['root']
    rootl, _, rootr = re.split(' ', root)
    s = checksign(monkeys, rootl, rootr)

    while not settled:

        humn = int(sum(hbounds)/2)

        newmonkeys = monkeys.copy()
        newmonkeys['humn'] = humn
        newmonkeys = monkeymath(newmonkeys)

        left = newmonkeys[rootl]
        right = newmonkeys[rootr]

        if left == right: 
            settled = True
        if left - right > 0: 
            hbounds[s[0]] = humn
        if left - right < 0:
            hbounds[s[1]] = humn

    return humn

monkeys = getmonkeys(getinput('21'))

print('Part 1:', int(monkeymath(monkeys.copy())['root']))
print('Part 2:', findhumn(monkeys.copy()))