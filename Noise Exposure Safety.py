"""
Bishal Nath
bishal.nath66@login.cuny.edu		
"""
noiseLvl = float(input("Enter noise level in decibels: "))
hours = float(input("Enter hours of exposure: "))
if (noiseLvl <= 85):
    if (hours <= 8):
        print("Safe")
    else:
        print("Caution")
elif (noiseLvl > 85 and noiseLvl <= 88):
    if (hours <= 4):
            print("Safe")
    else:
            print("Caution")
elif (noiseLvl > 88 and noiseLvl <= 91):
    if (hours <= 2):
        print("Safe")
    else:
        print("Caution")
elif (noiseLvl > 91 and noiseLvl <= 94):
    if (hours <= 1):
        print("Safe")
    else:
        print("Caution")
else:
     print("Unsafe")