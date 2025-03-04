from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.h_direction = 1
        self.v_direction = 1

    def move(self):
        new_x = self.xcor() + self.h_direction
        new_y = self.ycor() + self.v_direction
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.v_direction *= -1

    def bounce_x(self):
        self.h_direction *= -1

    def reset_ball(self):
        self.bounce_x()
        self.bounce_y()
        self.goto(0, 0)