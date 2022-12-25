# Day 25: Full of Hot Air

from _getinput import *

def getdecimal(SNAFU, total = 0):

    table = {'2':2, '1':1, '0':0, '-':-1, '=':-2}

    for snafu in SNAFU:

        snafu = list(snafu)
        snafu.reverse()

        place = 1; decimal = 0

        for s in snafu:
            decimal += table[s] * place
            place *= 5

        total += decimal

    return total

def getSNAFU(decimal, SNAFU = ''):

    table = {2:'2', 1:'1', 0:'0', 4:'-', 3:'='}
    
    while decimal:
        
        decimal, mod = divmod(decimal,5)
        SNAFU = table[mod] + SNAFU

        if mod in [3,4]: decimal += 1

    return SNAFU

decimal = getdecimal(getinput('25'))
SNAFU = getSNAFU(decimal)

print('The end:', SNAFU)