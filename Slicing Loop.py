"""
Bishal Nath
bishal.nath66@login.cuny.edu		
"""
s = str(input("Enter a string: "))
ls = len(s)
for i in range(ls - 1):
  print(s[:i])
  print(s[i:])
print("Closing statement?")