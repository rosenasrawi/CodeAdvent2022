# Day 19: Not Enough Minerals

from _getinput import *

from collections import deque
import re

def testblueprint(BP, limit):

    bp_num, ore4ore, ore4clay, ore4obs, clay4obs, ore4geo, obs4geo  = BP
    max_ore = max(ore4ore, ore4clay, ore4obs, ore4geo)

    start = ((1,0,0,0), (0,0,0,0), limit)

    queue = deque([start])
    visited = set()

    max_geo = 0

    while queue:

        robots, resources, time = queue.pop()

        ore_rob, clay_rob, obs_rob, geo_robs = robots
        ore, clay, obs, geo = resources

        if geo > max_geo: max_geo = geo

        if time == 0:
            continue

        ore = min(ore, max_ore + (max_ore - ore_rob) * (time -1))
        clay = min(clay, clay4obs + (clay4obs - clay_rob) * (time -1))
        obs = min(obs, obs4geo + (obs4geo - obs_rob) * (time -1))

        state = (robots, (ore,clay,obs,geo), time)

        if state in visited:
            continue

        visited.add(state)

        if ore >= ore4ore and ore_rob < max_ore: # Make ore robot
            
            robots = (ore_rob +1, clay_rob, obs_rob, geo_robs)
            resources = (ore + ore_rob - ore4ore, clay + clay_rob, obs + obs_rob, geo + geo_robs)
            
            queue.append((robots, resources, time -1))

        if ore >= ore4clay and clay_rob < clay4obs: # Make clay robot

            robots = (ore_rob, clay_rob +1, obs_rob, geo_robs)
            resources = (ore + ore_rob - ore4clay, clay + clay_rob, obs + obs_rob, geo + geo_robs)

            queue.append((robots, resources, time -1))

        if ore >= ore4obs and clay >= clay4obs and obs_rob < obs4geo: # Make obs robot

            robots = (ore_rob, clay_rob, obs_rob +1, geo_robs)
            resources = (ore + ore_rob - ore4obs, clay + clay_rob - clay4obs, obs + obs_rob, geo + geo_robs)

            queue.append((robots, resources, time -1))

        if ore >= ore4geo and obs >= obs4geo: # Make geo robot

            robots = (ore_rob, clay_rob, obs_rob, geo_robs +1)
            resources = (ore + ore_rob - ore4geo, clay + clay_rob, obs + obs_rob - obs4geo, geo + geo_robs)

            queue.append((robots, resources, time -1))

        # Or, don't make a robot
        robots = (ore_rob, clay_rob, obs_rob, geo_robs)
        resources = (ore + ore_rob, clay + clay_rob, obs + obs_rob, geo + geo_robs)

        queue.append((robots, resources, time -1))

    return bp_num, max_geo

blueprints = getinput('19')
blueprints = [list(map(int, re.findall(r'\d+', bp))) for bp in blueprints]

all = 0; three = 1

for BP in blueprints:
    bp_num, max_geo = testblueprint(BP, limit = 24)

    all += (bp_num * max_geo)

for BP in blueprints[:3]:
    bp_num, max_geo = testblueprint(BP, limit = 32)

    three *= max_geo

print('Part 1:', all)
print('Part 2:', three)