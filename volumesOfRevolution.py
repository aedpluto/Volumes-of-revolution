"""
Created on Fri Feb 28 19:24:08 2020
@author: amyed
Program to do 3D Modelling
"""

import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib.patches import Circle

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
circles = []

def drawCircle(radius, rev="x"):
    # Draw a circle on the x=0 'wall'
    circles.append(Circle((0, 0), radius*0.00005, fill=False))
    ax.add_patch(circles[-1])
    art3d.pathpatch_2d_to_3d(circles[-1], z=len(circles), zdir=rev)

#def plotShape(minLim, maxLim):
minLim=0; maxLim=400
for x in range(minLim, maxLim):
    try:
        drawCircle(15*1.9**(x/20))
    except Exception:
        pass
    
#def showDiagram(minLimAxes=-100, maxLimAxes=100):
minLimAxes=-100; maxLimAxes=500
ax.set_xlim(minLimAxes, maxLimAxes)
ax.set_ylim(minLimAxes, maxLimAxes)
ax.set_zlim(minLimAxes, maxLimAxes)
plt.show()

'''
# 100000* x**(1/2) * -1**(50-x)
# 80*(x)*(x-400)+1000
# 15*2**(x/20)
'''