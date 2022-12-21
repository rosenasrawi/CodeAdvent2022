# Day 21: Monkey Math

from _getinput import *
import re

def getmonkeys(input):

    monkeys = {}

    for m in input:
        m, oper = re.split(': ', m)
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
    else: return [1,0]

def findhumn(monkeys):

    root = monkeys['root']
    rootl, op, rootr = re.split(' ', root)

    settled = False
    hbounds = [0, int(5e14)]

    s = checksign(monkeys, rootl, rootr)

    while not settled:

        humn = int(sum(hbounds)/2)

        newmonkeys = monkeys.copy()
        newmonkeys['humn'] = humn
        newmonkeys = monkeymath(newmonkeys)

        left = newmonkeys[rootl]
        right = newmonkeys[rootr]

        if left == right: settled = True

        diff = left - right

        if diff > 0: 
            hbounds[s[0]] = humn
        if diff < 0:
            hbounds[s[1]] = humn

    return humn

monkeys = getmonkeys(getinput('21'))

newmonkeys = monkeymath(monkeys.copy())
root = int(newmonkeys['root'])
print('Part 1:', root)

humn = findhumn(monkeys.copy())
print('Part 2:', humn)