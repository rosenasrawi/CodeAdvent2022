# Day 10: Cathode-Ray Tube

from _preprocess import *

program = preprocess('10')

cycle = 0; x = 1
signal = [20,60,100,140,180,220]

def update(cycle,signal,x):
    cycle += 1
    if cycle in signal:
        signal[signal.index(cycle)] *= x

    return cycle,signal

for mes in program:

    cycle,signal = update(cycle,signal,x)

    if mes != 'noop':
        mes = mes.split()  
        cycle,signal = update(cycle,signal,x)
        x += int(mes[1])

print(sum(signal))