import os

def preprocess(day):

    with open(os.getcwd() + '/input/input-' + day + '.txt', "r") as input:
        data = input.readlines()
        data = [i.rstrip('\n') for i in data]

    return data