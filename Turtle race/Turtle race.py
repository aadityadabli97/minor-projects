Turtle race Project

# from turtle import Turtle,Screen
# x, y = -230, -100
# t=Turtle(shape="turtle")
# screen=Screen()
# screen.setup(width=500,height=400)
# screen.clear()
# colors = ["red", "yellow", "green", "blue", "cyan", "magenta"]
# user_bet=screen.textinput(title="Make you bet",prompt="Which turtle will win the race? Enter a color :")
# print(user_bet)
# for i in range(6):
#     t=Turtle(shape="turtle")
#     t.color(colors[i])
#     t.penup()
#     t.goto(x=x, y=y)
#     y+=40
#
# screen.exitonclick()
import turtle
from turtle import Turtle, Screen
import random

x, y = -230, -100
colors = ["red", "yellow", "green", "blue", "cyan", "magenta"]
turtles = list()
screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=400)
for i in range(6):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x=x, y=y)
    y+=40
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color :")
print(user_bet)
if user_bet:
    is_race_on=True

while is_race_on:

    for i in turtles:
        if i.xcor()>230:
            is_race_on=False
            winning_color=i.pencolor()
            if winning_color==user_bet:
                print(f"You've won ! The {winning_color} turtle is the winner !")
            else:
                print(f"You've lost ! The {winning_color} turtle is the winner!")
        rand_distance=random.randint(10,20)
        i.forward(rand_distance)

screen.exitonclick()
