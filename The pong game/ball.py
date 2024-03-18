from turtle import Turtle, Screen

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x=10
        self.y=10
        self.speed_ball=0.1

    def create_ball(self):
        self.shape("circle")
        self.color("white")

    def move_ball(self):
        self.penup()
        new_x=self.xcor()+self.x
        new_y=self.ycor()+self.y
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y=-self.y

    def bounce_x(self):
        self.x=-self.x
        self.speed_ball *=0.9

    def bounce_x_l_paddle(self):
        self.x = (abs(self.x))
        self.speed_ball *= 0.9

    def bounce_x_r_paddle(self):
        self.x = -(abs(self.x))
        self.speed_ball *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.speed_ball=0.1
        self.bounce_x()