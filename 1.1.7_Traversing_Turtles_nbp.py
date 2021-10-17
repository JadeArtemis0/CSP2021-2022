#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl
from turtle import xcor
from turtle import ycor
import turtle

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]
for shp in turtle_shapes:
  t = trtl.Turtle(shape=shp)
  my_turtles.append(t)
  trtl.begin_fill()
  new_color = turtle_colors.pop()
  t.fillcolor(new_color)
  t.pencolor(new_color)


#  starting Positions

startx = 0
starty = 0
startx =t.xcor()
starty =t.ycor()
trtl.penup()



#moving the turtle

for t in my_turtles:
  t.goto(startx, starty)
  for i in range(8):
      direction = 90
      direction = t.heading()
      t.setheading(direction)

      
      trtl.pendown()
      t.right(45)     
      t.forward(50)

#	new starting positions
  startx =  startx + 50
  starty = starty + 50
trtl.end_fill()
wn = trtl.Screen()
wn.mainloop()