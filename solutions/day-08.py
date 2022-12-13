# Day 8: Treetop Tree House

from _getinput import *

def viewdist(line, tree, v = 0):
    for t in line:
        v += 1
        if int(t) >= tree: break
    return v

def treehouse(trees, visible = 0, view = 0):

    visible += len(trees)*2 + (len(trees)-2)*2

    for r in range(1,len(trees)-1):

        hor = trees[r]

        for c in range(1,len(trees)-1):

            vert = ''.join([trees[i][c] for i in range(len(trees))])
            tree = int(trees[r][c])
            
            left = hor[:c][::-1]; right = hor[c+1:]; 
            top = vert[:r][::-1]; bottom = vert[r+1:]

            lvis = all(int(i) < tree for i in left)
            rvis = all(int(i) < tree for i in right)
            tvis = all(int(i) < tree for i in top)
            bvis = all(int(i) < tree for i in bottom)

            if lvis or rvis or tvis or bvis:
                visible += 1

            lview = viewdist(left,tree)
            rview = viewdist(right,tree)
            tview = viewdist(top,tree)
            bview = viewdist(bottom,tree)
            
            dist = lview*rview*tview*bview
            if view < dist: view = dist

    return visible, view

visible, view = treehouse(getinput('08'))

print('Part 1:', visible)
print('Part 2:', view)