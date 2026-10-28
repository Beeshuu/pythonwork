"""
Bishal Nath
bishal.nath66@login.cuny.edu		
"""
import numpy as np
import matplotlib.pyplot as plt

elevations = np.loadtxt('elevationsNYC.txt')

mapShape = elevations.shape + (3,)

floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0:
            floodMap[row,col,2] = 1.0     #Set the blue channel to 100%
        elif elevations[row,col] <= 6:
            floodMap[row,col,0] = 1.0     #Set the red channel to 100%
            floodMap[row,col,1] = 1.0   #Set the green channel to 100%

plt.imshow(floodMap)

plt.show()

plt.imsave('floodMap.png', floodMap)