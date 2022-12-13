import os

def getinput(day):

    with open(os.getcwd() + '/input/input-' + day + '.txt', "r") as input:
        data = input.readlines()
        data = [i.rstrip('\n') for i in data]
        if len(data) == 1: data = data[0]

    return data