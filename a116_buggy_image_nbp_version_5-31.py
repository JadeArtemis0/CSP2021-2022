#   a116_buggy_image.py
import turtle as trtl

painter = trtl.Turtle() #creates a spider body (5-7)
painter.pensize(40)
painter.circle(20)

#configures the spider body
is_eight = 8
is_seventy = 70
is_360 = 360 / is_eight
painter.pensize(5)
is_zero = 0
while (is_zero < is_eight): #Begins drawing legs (Side 1)
  painter.goto(0,20)
  painter.setheading(is_360*is_zero)
  painter.forward(is_seventy)
  is_zero = is_zero + 1

painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()