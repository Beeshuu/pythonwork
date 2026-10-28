"""
Bishal Nath
bishal.nath66@login.cuny.edu		
"""
word_count = 0
for i in range(5):
  phrase = input("Enter phrase: ")
  words = phrase.split()
  for word in words:
    word_count = word_count + 1
  print(word_count)
  word_count = 0