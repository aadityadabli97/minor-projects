from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()

    def create_paddle(self):
        """Create a new Paddle"""

        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.penup()

    def goup(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def godown(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

