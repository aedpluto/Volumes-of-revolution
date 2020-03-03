"""
Created on Fri Feb 28 19:24:08 2020
Program to do 3D Modelling
"""

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib.patches import Circle

# sets up plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
circles = []

# draws a single circle
def drawCircle(radius, rev="x"):
    # Draw a circle on the x=0 'wall'
    circles.append(Circle((0, 0), radius*0.00005, fill=False))
    ax.add_patch(circles[-1])
    art3d.pathpatch_2d_to_3d(circles[-1], z=len(circles), zdir=rev)

# creates the shape
minLim=0; maxLim=400
for x in range(minLim, maxLim):
    try:
        drawCircle(15*1.9**(x/20))
    except Exception:
        pass

# displays the graph
minLimAxes=-100; maxLimAxes=500
ax.set_xlim(minLimAxes, maxLimAxes)
ax.set_ylim(minLimAxes, maxLimAxes)
ax.set_zlim(minLimAxes, maxLimAxes)
plt.show()
