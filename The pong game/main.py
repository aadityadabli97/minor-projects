from turtle import Turtle, Screen
from Paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Setting up GUI
p1 = Paddle()
p2 = Paddle()
b=Ball()
scoreboard=Scoreboard()
screen = Screen()
screen.setup(width=800, height=600)
screen.colormode(255)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

p1.create_paddle()
p1.setpos(380, 0)
p2.create_paddle()
p2.setpos(-380, 0)

b.create_ball()

screen.listen()
screen.onkey(p1.goup, "Up")
screen.onkey(p1.godown, "Down")
screen.onkey(p2.goup, "w")
screen.onkey(p2.godown, "s")

game_is_on = True
while game_is_on:
    time.sleep(b.speed_ball)
    screen.update()
    b.move_ball()

    #Detect collision with wall
    if b.ycor()>280 or b.ycor()<-280:
        #needs to bounce
        b.bounce_y()

    #Detect collision with paddle
    # if b.distance(p1) < 50 and b.xcor() > 320 or b.distance(p2) < 50 and b.xcor() < -320:
    #     b.bounce_x()
    if b.distance(p1) < 50 and b.xcor() > 320:
        b.bounce_x_r_paddle()

    #Detect collision with left paddle
    if b.distance(p2) < 50 and b.xcor() < -320:
        b.bounce_x_l_paddle()
    #Detect right paddle if it misses

    if b.xcor() > 390:
        b.reset_position()
        scoreboard.l_score()

    #Detect left paddle if it misses

    if b.xcor() < -390:
        b.reset_position()
        scoreboard.r_score()

screen.exitonclick()
