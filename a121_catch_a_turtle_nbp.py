import turtle as trtl
import random as rand
# draws the circle
trtl.speed(0)
spot= trtl.Turtle
trtl.fillcolor("blue")

trtl.turtlesize(2)
trtl.shape("circle")


#draws the square behind the score
box = trtl.Turtle()
box.goto(100,0)
box.shape("square")
box.shapesize(3)

def change_position(new_xpos, new_ypos):
    spot.penup()
    new_xpos = rand.randint(-300, 300)
    new_ypos = rand.randint(-400, 400)
    spot.goto(new_xpos, new_ypos)
    spot.pendown()

def spot_clicked(x, y):
    change_position(x, y)

def update_score():
   global score
   score = 0
   score = score + 1
   print(score)

def update_score_for_box(x,y):
  global score # gives this function access to the score that was created above
  score += 1
  print(score)

def score_writer():
    spot.penup()
    spot.goto(100, 400)
    spot.pendown()


box = trtl.Turtle
trtl.update_score()
trtl.penup()
trtl.onclick(trtl.write("Arial", 20, "normal"))
trtl.pendown()
spot.onclick(change_position)
spot.onclick(spot_clicked)
score_writer()

wn = trtl.Screen
wn.mainloop()