# Day 10: Cathode-Ray Tube

from _preprocess import *

def update(cycle,signal,x):

    cycle += 1
    if cycle in signal:
        signal[signal.index(cycle)] *= x

    return cycle,signal

def response(pixels,letters,sprite):

    if len(pixels) in sprite: pixels += '🎁'
    else: pixels += '🎄'

    if len(pixels) == 40:
        letters.append(pixels); pixels = ''
    
    return pixels, letters

def decoder(program):
    
    cycle = 0; x = 1
    signal = [20,60,100,140,180,220]

    sprite = [0,1,2]
    pixels = ''; letters = []

    for mes in program:

        cycle,signal = update(cycle,signal,x)
        pixels,letters = response(pixels,letters,sprite)
        
        if mes != 'noop':
            mes = mes.split()  

            cycle,signal = update(cycle,signal,x)
            pixels,letters = response(pixels,letters,sprite)

            x += int(mes[1])
            sprite = [i+int(mes[1]) for i in sprite]
        
    print('Part 1:', sum(signal))

    for row in letters: print(row)

program = preprocess('10')
decoder(program)