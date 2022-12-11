# Day 11: Monkey in the Middle

from _preprocess import *
import re, math

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

input = preprocess('ex')
monkeys = getmonkeys(input)

for i in range(20):
    for m in range(len(monkeys)):

        while len(monkeys[m]['it']):

            num = monkeys[m]['it'].pop(0)
            monkeys[m]['insp']+=1

            operator = monkeys[m]['op']
            test = monkeys[m]['tst']

            num = operation(num, operator)
            num = math.floor(num/3)
            
            monkeys = throw(num, test, monkeys)

inspected = [monkeys[m]['insp'] for m in range(len(monkeys))]
inspected.sort()

print(inspected[-2]*inspected[-1])


