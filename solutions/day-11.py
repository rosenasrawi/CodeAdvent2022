# Day 11: Monkey in the Middle

from _getinput import *
import re, heapq, numpy

def getmonkeys(input, monkeys = {}):

    imonkeys = [i for i, line in enumerate(input) if 'Monkey' in line]

    for m,i in enumerate(imonkeys):
        monkeys[m] = {}
        monkeys[m]['it'] = list(map(int,re.findall(r'\d+', input[i+1])))
        monkeys[m]['op'] = input[i+2].split(' ')[-2:]
        monkeys[m]['tst'] = [int(input[i+n].split(' ')[-1]) for n in [3,4,5]]
        monkeys[m]['ins'] = 0

    return monkeys

def operate(num, operator):

    oper, val = operator

    if val == 'old': val = num
    else: val = int(val)

    if oper == '*': num *= val
    elif oper == '+': num += val

    return num

def throw(num, test, monkeys):

    div, m1, m2 = test

    if num%div == 0: monkeys[m1]['it'].append(num)
    else: monkeys[m2]['it'].append(num)

    return monkeys
    
def therapy(num,part,divisor):

    if part == 1: num //= 3
    else: num %= divisor

    return num

def monkeybusiness(monkeys, part, rounds, divisor = 1):

    divisor = numpy.prod([monkeys[m]['tst'][0] for m in range(len(monkeys))])

    for r in range(rounds):
        for m in range(len(monkeys)):

            while monkeys[m]['it']:
                monkeys[m]['ins'] += 1

                num = monkeys[m]['it'].pop(0)
                operator = monkeys[m]['op']
                test = monkeys[m]['tst']

                num = operate(num, operator)
                num = therapy(num,part,divisor)
                monkeys = throw(num, test, monkeys)

    inspected = [monkeys[m]['ins'] for m in range(len(monkeys))]

    return numpy.prod(heapq.nlargest(2,inspected))

input = getinput('11')

print('Part 1:', monkeybusiness(getmonkeys(input), 1, 20))
print('Part 2:', monkeybusiness(getmonkeys(input), 2, 10000))