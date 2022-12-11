# Day 11: Monkey in the Middle

from _preprocess import *
import re
import time

def operation(num, operator):
    oper, val = operator

    if val == 'old': val = num
    else: val = int(val)

    if oper == '*': num *= val
    elif oper == '+': num += val

    return num

def throw(num, test, monkeys):

    div, m1, m2 = test

    if num%div == 0:
        monkeys[m1]['it'].append(num)
    else:     
        monkeys[m2]['it'].append(num)

    return monkeys

def getmonkeys(input):

    imonkeys = [i for i, line in enumerate(input) if 'Monkey' in line]
    monkeys = {}

    for m,i in enumerate(imonkeys):

        monkeys[m] = {}
        monkeys[m]['it'] = list(map(int,re.findall(r'\d+', input[i+1])))
        monkeys[m]['op']  = input[i+2].split(' ')[-2:]
        monkeys[m]['tst']  = [int(input[i+n].split(' ')[-1]) for n in [3,4,5]]
        monkeys[m]['insp'] = 0

    return monkeys

def therapy(num, div, part):

    if part == 1: num //= 3
    else: num %= div

    return num

def monkeybusiness(monkeys, part):

    if part == 1: rounds = 20
    else: rounds = 10000
    
    divisor = 1
    for m in range(len(monkeys)):
        divisor *= monkeys[m]['tst'][0]

    for i in range(rounds):
        for m in range(len(monkeys)):

            while len(monkeys[m]['it']):

                num = monkeys[m]['it'].pop(0)
                monkeys[m]['insp']+=1

                operator = monkeys[m]['op']
                test = monkeys[m]['tst']

                num = operation(num, operator)
                num = therapy(num, divisor, part)

                monkeys = throw(num, test, monkeys)

    inspected = [monkeys[m]['insp'] for m in range(len(monkeys))]
    inspected.sort()

    return inspected[-2]*inspected[-1]

input = preprocess('11')

print('Part 1:', monkeybusiness(getmonkeys(input), 1))
print('Part 2:', monkeybusiness(getmonkeys(input), 2))