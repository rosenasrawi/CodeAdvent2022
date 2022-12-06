from _preprocess import *
from collections import Counter

signal = preprocess('06')[0]

def findstart(signal,plen):

    for i in range(len(signal)-plen-1):
        pack = signal[i:i+plen]
        if len(pack) == len(Counter(pack)):
            break

    return i+plen

print('Part 1:', findstart(signal,4))
print('Part 2:', findstart(signal,14))