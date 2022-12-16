# Day 16: Proboscidea Volcanium

from _getinput import *
import re

def getvalves(scanner, valves = {}, flows = {}):

    for out in scanner:
        v = list(map(str,re.findall(r'\b[A-Z]{2}\b', out)))
        f = int(re.findall(r'\d+', out)[0])
        valves[v[0]] = v[1:]
        flows[v[0]] = f

    return valves, flows

def dfs(flows, valves, stack = [(1,"AA", 0, ())], memory = {}, best = 0):

    while stack:

        state = stack.pop()
        time, location, score, opened = state
        opened = {x for x in opened}

        if memory.get((time,location), -1) >= score: # Had better score here before
            continue # Skip to the next iteration

        memory[(time,location)] = score # Save score for this time & location

        if time == 30:
            if score > best: best = score
            continue # Times up, so try next one

        flow = sum(flows[loc] for loc in opened)

        for neigh in valves[location]: # (1) go to neighbour
            newstate = (time+1, neigh, score+flow, tuple(opened))
            stack.append(newstate)

        if flows[location] > 0 and location not in opened: # (2) open the valve
            opened.add(location)
            flow = sum(flows[loc] for loc in opened)

            newstate = (time+1, location, score+flow, tuple(opened))
            stack.append(newstate)

    return best

def elephantdfs(flows, valves, stack = [(1, "AA", "AA", 0, ())], memory = {}, best = 0):

    while stack:

        state = stack.pop()
        time, me, elephant, score, opened = state
        opened = {x for x in opened}

        if memory.get((time,me,elephant), -1) >= score: # Had better score here before
            continue # Skip to the next iteration

        memory[(time,me,elephant)] = score # Save score for this time & location

        if time == 26:
            if score > best: best = score
            continue # Times up, so try next one

        flow = sum(flows[loc] for loc in opened)
        
        mecanopen = (flows[me] > 0 and me not in opened)
        elephantcanopen = (flows[elephant] > 0 and elephant not in opened)

        for neigh_me in valves[me]: # (1) Both go to neighbour
            for neigh_eleph in valves[elephant]:
                newstate = (time+1, neigh_me, neigh_eleph, score+flow, tuple(opened))
                stack.append(newstate)

        if elephantcanopen: # (2) Only elephant opens valve
            opened.add(elephant)
            flow = sum(flows[loc] for loc in opened)

            for neigh_me in valves[me]: 
                newstate = (time+1, neigh_me, elephant, score+flow, tuple(opened))
                stack.append(newstate)

            opened.discard(elephant) # remove for when they don't

        if mecanopen: # (3) Only I open valve
            opened.add(me)
            flow = sum(flows[loc] for loc in opened)

            for neigh_elephant in valves[elephant]:
                newstate = (time+1, me, neigh_elephant, score+flow, tuple(opened))
                stack.append(newstate)

            if elephantcanopen: # (4) Both open valve
                opened.add(elephant)
                flow = sum(flows[loc] for loc in opened)

                newstate = (time+1, me, elephant, score+flow, tuple(opened))
                stack.append(newstate)

    return best
 
valves, flows = getvalves(getinput('16'))

print('Part 1:', dfs(flows, valves))
print('Part 2:', elephantdfs(flows, valves))