# Day 3: Rucksack Reorganisation

from _getinput import *
import string

def split(sack):
    m = len(sack)//2
    return sack[:m], sack[m:]

letters = list(string.ascii_letters)
mappings = {let: val+1 for val, let in enumerate(letters)}

def elfsupplies(rucksacks, part, common = [], total = 0):

    if part == 1:

        for sack in rucksacks:
            s1, s2 = split(sack)

            for i in s1:
                if i in s2: common.append(i); break

    elif part == 2:

        for s in range(0,len(rucksacks),3):
            group = rucksacks[s:s+3]
            self = group.pop(group.index(max(group, key=len)))

            for i in self:
                if i in group[0] and i in group[1]: 
                    common.append(i); break

    for i in common: total += mappings[i]

    return total

rucksacks = getinput('03')

print('Part 1:', elfsupplies(rucksacks,1))
print('Part 2:', elfsupplies(rucksacks,2))