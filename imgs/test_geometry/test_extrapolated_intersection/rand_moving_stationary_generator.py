"""
This library displays sample problems that you can tweak and 
outputs them to console
"""


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

from utils import create_newfig, create_moving_polygon, create_still_polygon
import random
import math
import time

def test_collinear(pt1, pt2, pt3):
    Ax = pt1[0]
    Ay = pt1[1]
    Bx = pt2[0]
    By = pt2[1]
    Cx = pt3[0]
    Cy = pt3[1]
    return math.isclose(Ax * (By - Cy) + Bx * (Cy - Ay) + Cx * (Ay - By), 0, abs_tol=1e-07)

def gen_rand_poly_verts(minx, maxx, miny, maxy, minrad, maxrad):
    x_halfsteps = (maxx - minx) * 2
    y_halfsteps = (maxy - miny) * 2
    
    centerx = random.randint(3, x_halfsteps - 3)
    centery = random.randint(3, y_halfsteps - 3)
    
    centerx = minx + centerx / 2
    centery = miny + centery / 2
    
    result = []
    
    curr_angle = random.randint(0, 120)
    start_angle = curr_angle
    
    radx = random.uniform(minrad, maxrad)
    rady = radx
    finished = False
    while True:
        newpt = (centerx + round(math.cos(curr_angle * math.pi / 180) * radx), centery + round(math.sin(curr_angle * math.pi / 180) * rady))
        # the rounding makes this function pretty inaccurate and can have dupl points
        found = False
        for pt in result:
            if math.isclose(pt[0], newpt[0]) and math.isclose(pt[1], newpt[1]):
                found = True
                break
        if not found:
            collinear = False if len(result) < 3 else test_collinear(result[-2], result[-1], newpt)
            
            if not collinear:
                result.append(newpt)
        
        if finished:
            result.reverse()
            return result
        
        step = random.randint(5, 120)
        curr_angle = curr_angle + step
        if curr_angle >= 360:
            curr_angle -= 360
            if curr_angle > start_angle:
                result.reverse()
                return result
            finished = True
            
def get_rand_move_vec():
    dieroll = random.randint(0, 100)
    
    if dieroll < 10:
        return (0, random.randint(1, 10))
    elif dieroll < 20:
        return (0, -random.randint(1, 10))
    elif dieroll < 30:
        return (random.randint(1, 10), 0)
    elif dieroll < 40:
        return (-random.randint(1, 10), 0)
    else:
        return (random.randint(1, 10) * random.choice((-1, 1)), random.randint(1, 10) * random.choice((-1, 1)))

def gen_problem():
    stillpoly = gen_rand_poly_verts(-10, 20, -10, 10, 1, 3)
    movingpoly = gen_rand_poly_verts(-10, 20, -10, 10, 1, 3)
    movevec = get_rand_move_vec()
    
    xmin = 0
    xmin = min(xmin, min(p[0] for p in stillpoly))
    xmin = min(xmin, min(p[0] for p in movingpoly))
    xmin = min(xmin, min(p[0] + movevec[0] for p in movingpoly))
    
    xmax = 6
    xmax = max(xmax, max(p[0] for p in stillpoly))
    xmax = max(xmax, max(p[0] for p in movingpoly))
    xmax = max(xmax, max(p[0] + movevec[0] for p in movingpoly))
    
    ymin = 0
    ymin = min(ymin, min(p[1] for p in stillpoly))
    ymin = min(ymin, min(p[1] for p in movingpoly))
    ymin = min(ymin, min(p[1] + movevec[1] for p in movingpoly))
    
    ymax = 4
    ymax = max(ymax, max(p[1] for p in stillpoly))
    ymax = max(ymax, max(p[1] for p in movingpoly))
    ymax = max(ymax, max(p[1] + movevec[1] for p in movingpoly))
    
    return stillpoly, movingpoly, movevec, (math.floor(xmin) - 1, math.ceil(xmax) + 1), (math.floor(ymin) - 1, math.ceil(ymax) + 1)

def make_tup_to_string(tup):
    pretty_x = tup[0]
    if math.isclose(int(tup[0]), tup[0], abs_tol=1e-07):
        pretty_x = int(tup[0])
    
    pretty_y = tup[1]
    if math.isclose(int(tup[1]), tup[1], abs_tol=1e-07):
        pretty_y = int(tup[1])
    return '({}, {})'.format(pretty_x, pretty_y)
    
def make_pts_to_string(tuples):
    return '({})'.format(', '.join(make_tup_to_string(tup) for tup in tuples))
    
def save_problem(stillpoly, movingpoly, movevec, xlim, ylim):
    mpolystr = make_pts_to_string(movingpoly)
    spolystr = make_pts_to_string(stillpoly)
    mvecstr = make_tup_to_string(movevec)
    
    # this is setup for how i copy+paste the result
    print('--graph--')
    print('xlim=({}, {}), ylim=({}, {}))'.format(xlim[0], xlim[1], ylim[0], ylim[1]))
    print('    create_moving_polygon(fig, ax, renderer, {}, {})'.format(mpolystr, mvecstr))
    print('    create_still_polygon(fig, ax, renderer, {})'.format(spolystr))
    print('    #fn({}, {}, {}, {})'.format(mpolystr, '(0, 0)', mvecstr, spolystr))
    
def gen_figure(stillpoly, movingpoly, movevec, xlim, ylim):
    fig, ax, renderer = create_newfig('rand', xlim=xlim, ylim=ylim)
    create_moving_polygon(fig, ax, renderer, movingpoly, movevec)
    create_still_polygon(fig, ax, renderer, stillpoly)
    return fig, ax
    
def show_figure(fig, ax):
    plt.ion()
    plt.show()
    
def delete_figure(fig, ax):
    plt.clf()
    plt.cla()
    plt.close('all')

stillpoly, movingpoly, movevec, xlim, ylim = gen_problem()
save_problem(stillpoly, movingpoly, movevec, xlim, ylim)
fig, ax = gen_figure(stillpoly, movingpoly, movevec, xlim, ylim)
show_figure(fig, ax)
    
while True:
    input("Press [enter] to continue.")
    print('generating new figure')
    delete_figure(fig, ax)
    plt.pause(0.001)
    stillpoly, movingpoly, movevec, xlim, ylim = gen_problem()
    save_problem(stillpoly, movingpoly, movevec, xlim, ylim)
    fig, ax = gen_figure(stillpoly, movingpoly, movevec, xlim, ylim)
    show_figure(fig, ax)
    plt.pause(0.001)