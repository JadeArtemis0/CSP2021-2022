import turtle as trtl
import turtle as score
score_writer = score.Turtle()
import random as rand
score = 0
#defining score writer
font_setup = ("Arial", 20, "normal")

#Draws and sets up the timer
timer = 30
counter_interval = 1000
timer_up = False

counter = trtl.Turtle()
def countdown():
  counter.goto(100, 120)
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 


# draws the circle
spot = trtl.Turtle()
spot.fillcolor("blue")
spot.speed(0)
spot.turtlesize(2)
spot.shape("circle")


score_writer.penup()
score_writer.goto(100, -100)
score_writer.pendown()

def change_position():
    spot.penup()
    new_xpos = rand.randint(-300, 300)
    new_ypos = rand.randint(-400, 400)
    spot.goto(new_xpos, new_ypos)
    spot.pendown()

def spot_clicked(x, y):
    global timer
    if timer < 30000:
        trtl.update_score()
        change_position()
        score_writer.clear()
    else:
        trtl.hideturtle()


def update_score():
   global score
   score = score + 1
   score_writer.write(score, font=font_setup)

spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn = trtl.Screen()
wn.mainloop()