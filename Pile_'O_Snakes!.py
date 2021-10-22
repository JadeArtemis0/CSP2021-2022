#time to make a pile of snakes!!
import turtle as tr
from turtle import *
tr.speed(0)
#begins drawing the background 
#Sourse is: https://dev.to/taarimalta/how-to-draw-a-spiral-with-python-turtle-2n5c
tr.pencolor("magenta")
tr.pensize(4)
tr.goto(5,5)
for i in range(180):
    tr.fd(i)
    tr.right(30)
tr.penup()
tr.pencolor("cyan")
tr.pensize(6)
tr.goto(0,0)
tr.pendown()
for i in range(180):
    tr.fd(i)
    tr.right(30)
tr.penup()
is_zero = 0
while is_zero <6:
    tr.left(60)
    #draws the shading on the snake (the shadow)
    tr.speed(7)
    tr.goto(0,-15)
    tr.pendown()
    tr.pensize(15)
    tr.pencolor("black")
    tr.circle(-40, 180)
    tr.circle(-50,180)
    tr.circle(50, 180)
    tr.circle(-30, 180)
    tr.penup()

    #Draws the snake body in navy blue
    snake_color = (input("What color do you want your snake to be?"))
    tr.speed(7)
    tr.goto(5,-15)
    tr.pendown()
    tr.pensize(15)
    tr.pencolor(snake_color)
    tr.circle(-40, 180)
    tr.circle(-50,180)
    tr.circle(50, 180)
    tr.circle(-30, 180)

    #Draws the snake head

    tr.color(snake_color)
    tr.shape("circle")
    tr.stamp()

    #draws eyes (part 1)

    tr.turtlesize(0.5)
    tr.pensize(0.5)
    tr.pencolor("white")
    tr.stamp()

    is_zero = is_zero + 1

tr.color("black")
snake_name = (input("What would you like to name your pile of snakes?"))
write(snake_name, align ="center", font = ("Times New Roman", 25))

wn = tr.Screen()
wn.mainloop()