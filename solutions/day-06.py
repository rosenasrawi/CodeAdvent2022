from _getinput import *
from collections import Counter

def findstart(signal,plen):
    for i in range(len(signal)-plen-1):
        if len(Counter(signal[i:i+plen])) == plen:
            return i+plen; break

signal = getinput('06')[0]
print('Part 1:', findstart(signal,4))
print('Part 2:', findstart(signal,14))