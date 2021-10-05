import turtle as trtl

ladybug = trtl.Turtle()

#Draws ladybug legs
is_six = 6
is_fifty = 50
is_360 = 360 / is_six
ladybug.pensize(5)
is_zero = 0
while (is_zero < is_six): #Begins drawing legs (Side 1)
  ladybug.goto(0, -60)
  ladybug.setheading(is_360*is_zero)
  ladybug.forward(is_fifty)
  is_zero = is_zero + 1

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

# and body +line
ladybug.penup()
ladybug.goto(0, -75) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
# + line (down the middle of the body)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(90)

# config dots
num_dots = 0
xpos = -20
ypos = -30
ladybug.pensize(10)

# draw two sets of dots

while (num_dots <= 2):
    ladybug.penup()
    ladybug.goto(xpos, ypos)
    ladybug.pendown()
    ladybug.circle(3)
    ladybug.penup()
    ypos = ypos + -30
    xpos = xpos + 5
    ladybug.goto(xpos + 30, ypos + 20)
    ladybug.pendown()
    ladybug.circle(2)
    num_dots = num_dots + 1

# position next dots
    num_dots = num_dots + 1




ladybug.hideturtle()
