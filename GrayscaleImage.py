"""
Bishal Nath
bishal.nath66@login.cuny.edu		
"""
import numpy as np
import matplotlib.pyplot as plt

intImageName = input("Enter the name of the input file: ")
outImageName = input("Enter the name of the output file: ")

intImage = plt.imread(intImageName)
for i in range(intImage.shape[0]):
    for j in range(intImage.shape[1]):
        intImage[i,j,0] = intImage[i,j,1] 
        intImage[i,j,2] = intImage[i,j,1]

plt.imsave(outImageName, intImage)
