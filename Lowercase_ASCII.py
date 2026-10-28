"""
Bishal Nath
bishal.nath66@login.cuny.edu		
"""
userstring = input("Enter a phrase: ")
userstring = userstring.lower()
currentstring = ""
for i in range(len(userstring)):
  currentstring = ord(userstring[i])
  print(userstring[i], end=" ")
  print(currentstring)