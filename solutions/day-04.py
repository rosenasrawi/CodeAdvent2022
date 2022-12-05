# Day 4: Camp Cleanup

from _preprocess import *
import re

def findoverlap(assignments, full=0, part=0):

    for asg in assignments:
        
        asg = list(map(int,re.split('-|,', asg)))

        overlap = (asg[0] >= asg[2] and asg[1] <= asg[3]) or (asg[2] >= asg[0] and asg[3] <= asg[1])
        if overlap: full += 1

        s1 = list(range(asg[0],asg[1]+1))
        s2 = list(range(asg[2],asg[3]+1))

        for i in s1:
            if i in s2: part += 1; break      

    print('Part 1:', full, ',', 'Part 2:', part)

assignments = preprocess('04')
findoverlap(assignments)