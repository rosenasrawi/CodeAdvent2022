# Day 19: Not Enough Minerals

from _getinput import *

from collections import deque
import re

def testblueprint(blueprint, limit):

    bp, o4o, o4c, o4ob, c4ob, o4g, ob4g = blueprint
    omax = max(o4o, o4c, o4ob, o4g)

    start = ((1,0,0,0), (0,0,0,0), limit)

    queue = deque([start])
    visited = set()

    maxgeode = 0

    while queue:

        robots, resources, time = queue.pop()

        orob, crob, obrob, grob = robots
        ore, clay, obs, geo = resources

        if geo > maxgeode: maxgeode = geo

        if time == 0:
            continue

        ore = min(ore, omax + (omax - orob) * (time -1))
        clay = min(clay, c4ob + (c4ob - crob) * (time -1))
        obs = min(obs, ob4g + (ob4g - obrob) * (time -1))

        state = (robots, (ore,clay,obs,geo), time)

        if state in visited:
            continue

        visited.add(state)

        if ore >= o4o and orob < omax: # Make ore robot
            
            robots = (orob +1, crob, obrob, grob)
            resources = (ore + orob - o4o, clay + crob, obs + obrob, geo + grob)
            
            queue.append((robots, resources, time -1))

        if ore >= o4c and crob < c4ob: # Make clay robot

            robots = (orob, crob +1, obrob, grob)
            resources = (ore + orob - o4c, clay + crob, obs + obrob, geo + grob)

            queue.append((robots, resources, time -1))

        if ore >= o4ob and clay >= c4ob and obrob < ob4g: # Make obs robot

            robots = (orob, crob, obrob +1, grob)
            resources = (ore + orob - o4ob, clay + crob - c4ob, obs + obrob, geo + grob)

            queue.append((robots, resources, time -1))

        if ore >= o4g and obs >= ob4g: # Make geo robot

            robots = (orob, crob, obrob, grob +1)
            resources = (ore + orob - o4g, clay + crob, obs + obrob - ob4g, geo + grob)

            queue.append((robots, resources, time -1))

        # Or, don't make a robot
        robots = (orob, crob, obrob, grob)
        resources = (ore + orob, clay + crob, obs + obrob, geo + grob)

        queue.append((robots, resources, time -1))

    return bp, maxgeode

blueprints = getinput('19')
blueprints = [list(map(int, re.findall(r'\d+', bp))) for bp in blueprints]

all = 0; three = 1

for blueprint in blueprints:
    bp, maxgeode = testblueprint(blueprint, limit = 24)

    all += (bp * maxgeode)

for blueprint in blueprints[:3]:
    bp, maxgeode = testblueprint(blueprint, limit = 32)

    three *= maxgeode

print('Part 1:', all)
print('Part 2:', three)