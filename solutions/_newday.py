from datetime import date

today = date.today()
day = today.strftime('%d')

solfile = 'day-' + day + '.py'
f = open('solutions/' + solfile, 'x')       # Returns error if file already exists
f.write('from _preprocess import *')        

inpfile = 'input-' + day + '.txt'
i = open('input/' + inpfile, 'x')