# Day 4 - Camp Cleanup

from _preprocess import *
import re

def partoverlap(assignments, total = 0):

    for asg in assignments:

        overlap = (asg[0] >= asg[2] and asg[1] <= asg[3]) or (asg[2] >= asg[0] and asg[3] <= asg[1])
        if overlap: total += 1

    print('Part 1:', total)

def fulloverlap(assignments, total = 0):

    for asg in assignments:

        s1 = list(range(asg[0],asg[1]+1))
        s2 = list(range(asg[2],asg[3]+1))

        for i in s1:
            if i in s2: total +=1; break

    print('Part 2:', total)
    
assignments = preprocess('04')
assignments = [list(map(int,re.split('-|,', asg))) for asg in assignments]

partoverlap(assignments); fulloverlap(assignments)