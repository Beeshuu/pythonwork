"""
Bishal Nath
bishal.nath66@login.cuny.edu		
"""

import pandas as pd

fileName = input("Enter CSV file name: ")
temp = pd.read_csv(fileName)
print(temp.groupby('Location')['Temperature'].min())
