from turtle import Turtle
import time
import random
SPEED = 1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(0, 0)
        self.color("white")
        self.x_speed = SPEED
        self.y_speed = SPEED

    def move(self):
        x_cor = self.xcor() + self.x_speed
        y_cor = self.ycor() + self.y_speed
        self.goto(x_cor, y_cor)

    def wall_bounce(self):
        self.y_speed *= -1.1

    def paddle_bounce(self):
        self.x_speed *= -1.1

    def ball_reset(self):
        self.goto(0, 0)
        self.x_speed *= random.choice((SPEED, -SPEED))
        self.y_speed *= random.choice((SPEED, -SPEED))
        self.screen.update()
