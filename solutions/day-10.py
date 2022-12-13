# Day 10: Cathode-Ray Tube

from _getinput import *

def draw(pixels,message,sprite):

    if len(pixels) in sprite: pixels += '🎁'
    else: pixels += '🎄'

    if len(pixels) == 40:
        message.append(pixels); pixels = ''
    
    return pixels, message

def cathode(program):

    x = 1; signal = [x]
    targets = [20,60,100,140,180,220]

    sprite = [0,1,2]
    pixels = ''; message = []

    for mes in program:

        signal.append(x)
        pixels, message = draw(pixels,message,sprite)

        if mes != 'noop':
            num = int(mes.split()[1])

            x += num
            signal.append(x)

            pixels, message = draw(pixels,message,sprite)
            sprite = [i+num for i in sprite]
    
    strenght = sum([signal[t-1]*t for t in targets])    
    
    return strenght, message

strenght, message = cathode(getinput('10'))

print('Part 1:', strenght)
for row in message: print(row)

# 🎁🎁🎁🎄🎄🎄🎁🎁🎄🎄🎁🎄🎄🎁🎄🎁🎁🎁🎁🎄🎄🎁🎁🎄🎄🎁🎄🎄🎄🎄🎁🎄🎄🎁🎄🎄🎁🎁🎄🎄
# 🎁🎄🎄🎁🎄🎁🎄🎄🎁🎄🎁🎄🎄🎁🎄🎁🎄🎄🎄🎄🎁🎄🎄🎁🎄🎁🎄🎄🎄🎄🎁🎄🎄🎁🎄🎁🎄🎄🎁🎄
# 🎁🎄🎄🎁🎄🎁🎄🎄🎄🎄🎁🎁🎁🎁🎄🎁🎁🎁🎄🎄🎁🎄🎄🎄🎄🎁🎄🎄🎄🎄🎁🎄🎄🎁🎄🎁🎄🎄🎄🎄
# 🎁🎁🎁🎄🎄🎁🎄🎁🎁🎄🎁🎄🎄🎁🎄🎁🎄🎄🎄🎄🎁🎄🎁🎁🎄🎁🎄🎄🎄🎄🎁🎄🎄🎁🎄🎁🎄🎁🎁🎄
# 🎁🎄🎄🎄🎄🎁🎄🎄🎁🎄🎁🎄🎄🎁🎄🎁🎄🎄🎄🎄🎁🎄🎄🎁🎄🎁🎄🎄🎄🎄🎁🎄🎄🎁🎄🎁🎄🎄🎁🎄
# 🎁🎄🎄🎄🎄🎄🎁🎁🎁🎄🎁🎄🎄🎁🎄🎁🎄🎄🎄🎄🎄🎁🎁🎁🎄🎁🎁🎁🎁🎄🎄🎁🎁🎄🎄🎄🎁🎁🎁🎄