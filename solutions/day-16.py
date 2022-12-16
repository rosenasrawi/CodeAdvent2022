# Day 16: Proboscidea Volcanium

from _getinput import *
import re

scanner = getinput('ex')

valves = {}
flows = {}

for out in scanner:
    v = list(map(str,re.findall(r'\b[A-Z]{2}\b', out)))
    f = int(re.findall(r'\d+', out)[0])
    valves[v[0]] = v[1:]
    flows[v[0]] = f

print(valves)
print(flows)

def dfs(flows, valves):

    stack = [(1,"AA", 0, ())]
    memory = {}
    best = 0

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

        # (1) go to neighbour:
        flow = sum(flows[loc] for loc in opened)
        for neigh in valves[location]:
            newstate = (time+1, neigh, score+flow, tuple(opened))
            stack.append(newstate)

        # (2) open the valve:
        if flows[location] > 0 and location not in opened:
            opened.add(location)
            flow = sum(flows[loc] for loc in opened)

            newstate = (time+1, location, score+flow, tuple(opened))
            stack.append(newstate)
    print(memory)
    return best
            
print(dfs(flows, valves))


# values = {'t':1, 'start': 'AA', 'score': 0, 'path': ['AA']}

# def dfs(flows, valves, values):

#     queue = [(1, 'AA', 0, ('AA',))]
#     visited = {}
#     best = 0

#     while queue:
#         next = queue.pop()
#         time, loc, score, opened = next

#         if visited.get((time,loc), -1) >= score:
#             continue

#         visited[(time,loc)] = score

def solve(flows, valves):

    states = [(1, "AA", 0, ())]
    seen = {}
    best = 0

    while len(states) > 0:

        current = states.pop()
        time, where, score, opened_s = current
        opened = {x for x in opened_s}

        if seen.get((time, where), -1) >= score:
            continue

        seen[(time, where)] = score

        if time == 30:
            best = max(best, score)
            continue

        # if we don't open a valve here

        new_score = score + sum(flows.get(where, 0) for where in opened)
        for option in valves[where]:
            new_state = (time + 1, option, new_score, tuple(opened))
            states.append(new_state)

        # if we open the valve here
        if flows[where] > 0 and where not in opened:

            opened.add(where)
            # new_score = score + sum(flows.get(where, 0) for where in opened)
            new_score = score + sum(flows[loc] for loc in opened) 
            new_state = (time + 1, where, new_score, tuple(opened))

            states.append(new_state)
            # opened.discard(where)


    return best

# print(solve(flows, valves))

# def find_all_paths(graph, start, end, path=[]):

#     path = path + [start]
#     if start == end:
#         return [path]

#     paths = []

#     for node in graph[start]:
#         if node not in path:
#             newpaths = find_all_paths(graph, node, end, path)
#             for newpath in newpaths:
#                 paths.append(newpath)

#     return paths

# print(find_all_paths(valves, 'AA', 'BB'))