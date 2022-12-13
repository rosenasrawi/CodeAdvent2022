from datetime import date
from aocd import get_data

today = date.today()
day = today.strftime('%d')

input = get_data(day = int(day), year = 2022)

inpfile = 'input-' + day + '.txt'
i = open('input/' + inpfile, 'x')           # Returns error if file already exists
i.write(input)

solfile = 'day-' + day + '.py'
f = open('solutions/' + solfile, 'x')       # Returns error if file already exists
f.write('from _getinput import *')