"""
Bishal Nath
bishal.nath66@login.cuny.edu		
"""
import turtle
t = turtle.Turtle()
t.speed(0)
for i in range(5):
  angle = int(input("Enter a number: "))
  t.left(angle)
  t.forward(100)