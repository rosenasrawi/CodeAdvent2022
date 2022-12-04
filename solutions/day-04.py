# Day 4 - Camp Cleanup

from _preprocess import *
import re

def findoverlap(assignments, part=0, full=0):

    for asg in assignments:

        overlap = (asg[0] >= asg[2] and asg[1] <= asg[3]) or (asg[2] >= asg[0] and asg[3] <= asg[1])
        if overlap: part += 1   

        s1 = list(range(asg[0],asg[1]+1))
        s2 = list(range(asg[2],asg[3]+1))

        for i in s1:
            if i in s2: full += 1; break      

    print('Part 1:', part, ',', 'Part 2:', full)

assignments = preprocess('04')
assignments = [list(map(int,re.split('-|,', asg))) for asg in assignments]

findoverlap(assignments)