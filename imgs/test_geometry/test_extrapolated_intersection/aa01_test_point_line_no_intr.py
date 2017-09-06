import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
renderer = fig.canvas.get_renderer()
plt.xlim(-1, 7)
plt.ylim(-1, 5)

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

moving_pt = plt.scatter([1], [1], zorder=5)

moving_pt_an = plt.annotate(s="(1, 1)", xy=(1, 1), zorder=5)
moving_pt_extents = moving_pt_an.get_window_extent(renderer)
moving_pt_an.remove()
moving_pt_an = ax.annotate(s="(1, 1)", xy=(1, 1), xytext=(-moving_pt_extents.width - 5, 5), textcoords='offset pixels', zorder=5)

moving_pt_ar = ax.annotate("", xy=(1, 1), xytext=(6, 1), arrowprops=dict(arrowstyle="<-", shrinkA=0, shrinkB=0, zorder=4))

segment_pts = ax.scatter([2, 6], [4, 2], c='r', zorder=5)
segment_arrow = ax.annotate("", xy=(2, 4), xytext=(6, 2), arrowprops=dict(arrowstyle="-", shrinkA=0, shrinkB=0, color='b', zorder=4))

an24 = ax.annotate('(2, 4)', xy=(2, 4), xytext=(5, 5), textcoords='offset pixels')
an62 = ax.annotate('(6, 2)', xy=(6, 2), xytext=(5, 5), textcoords='offset pixels')

plt.show()