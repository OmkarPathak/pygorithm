"""
Collection of functions that make making graphs easier.
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import sys

def prepare_figure(fig, ax, title):
    fig.suptitle(title)
    ax.set_xlim(-1, 7)
    ax.set_ylim(-1, 5)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.grid(True, linestyle='dashed')
    ax.xaxis.get_major_ticks()[0].label1.set_visible(False)
    ax.xaxis.get_major_ticks()[1].label1.set_visible(False)
    ax.xaxis.get_major_ticks()[-1].label1.set_visible(False)
    ax.yaxis.get_major_ticks()[0].label1.set_visible(False)
    ax.yaxis.get_major_ticks()[1].label1.set_visible(False)
    ax.yaxis.get_major_ticks()[-1].label1.set_visible(False)
    ax.xaxis.get_majorticklines()[0].set_visible(False)
    ax.xaxis.get_majorticklines()[-2].set_visible(False)
    ax.yaxis.get_majorticklines()[0].set_visible(False)
    ax.yaxis.get_majorticklines()[-2].set_visible(False)
    ax.xaxis.get_gridlines()[0].set_visible(False)
    ax.xaxis.get_gridlines()[-1].set_visible(False)
    ax.yaxis.get_gridlines()[0].set_visible(False)
    ax.yaxis.get_gridlines()[-1].set_visible(False)

def annotate_point(fig, ax, renderer, ptx, pty, dir, **kwargs):
    anstr = "({}, {})".format(ptx, pty)
    
    an = ax.annotate(s=anstr, xy=(ptx, pty), **kwargs)
    an_extents = an.get_window_extent(renderer)
    an.remove()
    
    offsetx = 0
    offsety = 0
    if dir == 'left':
        offsetx = -an_extents.width - 5
        offsety = -an_extents.height / 2
    elif dir == 'topleft':
        offsetx = -an_extents.width - 5
        offsety = 5
    elif dir == 'top':
        offsetx = -an_extents.width / 2
        offsety = 5
    elif dir == 'topright':
        offsetx = 5
        offsety = 5
    elif dir == 'right':
        offsetx = 5
        offsety = -an_extents.height / 2
    elif dir == 'botright':
        offsetx = 5
        offsety = -an_extents.height - 5
    elif dir == 'bot':
        offsetx = -an_extents.width / 2
        offsety = -an_extents.height - 5
    elif dir == 'botleft':
        offsetx = -an_extents.width - 5
        offsety = -an_extents.height - 5
    
    return ax.annotate(s=anstr, xy=(ptx, pty), xytext=(offsetx, offsety), textcoords='offset pixels', **kwargs)

def create_moving_point(fig, ax, renderer, ptx, pty, arendx, arendy, dir='botleft'):
    pt = ax.scatter([ptx], [pty], zorder=5)
    
    an = annotate_point(fig, ax, renderer, ptx, pty, dir, zorder=5)
    
    ar = ax.annotate("", xy=(ptx, pty), xytext=(arendx, arendy), arrowprops=dict(arrowstyle="<-", shrinkA=0, shrinkB=0, zorder=4, mutation_scale=15))
    return pt, an, ar

def create_moving_line(fig, ax, renderer, pt1tup, pt2tup, movetup, dir='botleft', dir2=None):
    dir2 = dir if dir2 is None else dir2
    pts = ax.scatter([pt1tup[0], pt2tup[0]], [pt1tup[1], pt2tup[1]], zorder=5)
    anpt1 = annotate_point(fig, ax, renderer, pt1tup[0], pt1tup[1], dir, zorder=5)
    anpt2 = annotate_point(fig, ax, renderer, pt2tup[0], pt2tup[1], dir2, zorder=5)
    
    conn_arrow = ax.annotate("", xy=pt1tup, xytext=pt2tup, arrowprops=dict(arrowstyle="-", shrinkA=0, shrinkB=0, color='g', zorder=4))
    
    move_pt1_arrow = ax.annotate("", xy=pt1tup, xytext=(pt1tup[0] + movetup[0], pt1tup[1] + movetup[1]), arrowprops=dict(arrowstyle="<-", linestyle=":", shrinkA=0, shrinkB=0, zorder=4, mutation_scale=15))
    move_pt2_arrow = ax.annotate("", xy=pt2tup, xytext=(pt2tup[0] + movetup[0], pt2tup[1] + movetup[1]), arrowprops=dict(arrowstyle="<-", linestyle=":", shrinkA=0, shrinkB=0, zorder=4, mutation_scale=15))
    
    #end_pts = ax.scatter([pt1tup[0] + movetup[0], pt2tup[0] + movetup[0]], [pt1tup[1] + movetup[1], pt2tup[1] + movetup[1]], zorder=5)
    end_pts_conn = ax.annotate("", xy=(pt1tup[0] + movetup[0], pt1tup[1] + movetup[1]), xytext=(pt2tup[0] + movetup[0], pt2tup[1] + movetup[1]), arrowprops=dict(arrowstyle="-", shrinkA=0, shrinkB=0, color='k', zorder=4, linestyle="dashed"))
    return pts, anpt1, anpt2, move_pt1_arrow, move_pt2_arrow, end_pts_conn
    
def create_moving_polygon(fig, ax, renderer, points, move, dir='botleft'):
    pointsx = list(p[0] for p in points)
    pointsy = list(p[1] for p in points)
    ax.scatter(pointsx, pointsy, zorder=5)
    
    last = points[-1]
    for p in points:
        pdir = p[2] if len(p) > 2 else dir
        annotate_point(fig, ax, renderer, p[0], p[1], pdir, zorder=5)
        
        ax.annotate("", xy=(last[0], last[1]), xytext=(p[0], p[1]), arrowprops=dict(arrowstyle="-", shrinkA=0, shrinkB=0, color='g', zorder=4))
        ax.annotate("", xy=(p[0], p[1]), xytext = (p[0] + move[0], p[1] + move[1]), arrowprops=dict(arrowstyle="<-", linestyle=":", shrinkA=0, shrinkB=0, zorder=4, mutation_scale=15))
        ax.annotate("", xy=(last[0] + move[0], last[1] + move[1]), xytext=(p[0] + move[0], p[1] + move[1]), arrowprops=dict(arrowstyle="-", shrinkA=0, shrinkB=0, color='k', zorder=4, linestyle="dashed"))
        
        last = p
    
def create_still_segment(fig, ax, renderer, pt1tup, pt2tup, dir='botleft', dir2=None):
    dir2 = dir if dir2 is None else dir2
    
    segment_pts = ax.scatter([ pt1tup[0], pt2tup[0] ], [ pt1tup[1], pt2tup[1] ], c='r', zorder=5)
    segment_arrow = ax.annotate("", xy=pt1tup, xytext=pt2tup, arrowprops=dict(arrowstyle="-", shrinkA=0, shrinkB=0, color='b', zorder=4))
    an1 = annotate_point(fig, ax, renderer, pt1tup[0], pt1tup[1], dir, zorder=5)
    an2 = annotate_point(fig, ax, renderer, pt2tup[0], pt2tup[1], dir2, zorder=5)
    return segment_pts, segment_arrow, an1, an2

def create_still_polygon(fig, ax, renderer, points, dir='botleft'):
    pointsx = list(p[0] for p in points)
    pointsy = list(p[1] for p in points)
    ax.scatter(pointsx, pointsy, zorder=5)
    
    last = points[-1]
    for p in points:
        pdir = p[2] if len(p) > 2 else dir
        annotate_point(fig, ax, renderer, p[0], p[1], pdir, zorder=5)
        
        ax.annotate("", xy=(last[0], last[1]), xytext=(p[0], p[1]), arrowprops=dict(arrowstyle="-", shrinkA=0, shrinkB=0, color='b', zorder=4))
        last = p

def create_newfig(title):
    fig, ax = plt.subplots()
    renderer = fig.canvas.get_renderer()
    prepare_figure(fig, ax, title)
    return fig, ax, renderer
    
def run_or_export(*args):
    fns = args
    
    figaxtitletups = []
    for fn in fns:
        figaxtitletups.append(fn())
        
    found_export_command = False
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == '--export':
            found_export_command = True
        else:
            print('Unknown Command: {}'.format(sys.argv[i]))

    if found_export_command:
        for fig, ax, longtitle in figaxtitletups:        
            fig.savefig('out/{}.png'.format(longtitle))
    else:
        plt.show()