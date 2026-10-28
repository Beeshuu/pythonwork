#Import the libraries for arrays and displaying images:
import numpy as np
import matplotlib.pyplot as plt

#Read in the data to an array, called elevations:
elevations = np.loadtxt('elevationsNYC.txt')
#Load the array into matplotlib.pyplot:
plt.imshow(elevations)
#Display the plot:
plt.show()
