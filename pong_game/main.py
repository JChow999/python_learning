import turtle
import paddle
import ball
import time
from scoreboard import ScoreBoard
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = "Black"

screen = turtle.Screen()
screen.bgcolor(SCREEN_COLOR)
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.listen()
screen.tracer(0)

middle_drawer = turtle.Turtle()
middle_drawer.penup()
middle_drawer.speed(0)
middle_drawer.hideturtle()
middle_drawer.pencolor("white")
middle_drawer.setheading(270)
half_height = SCREEN_HEIGHT / 2
middle_drawer.goto(0, half_height)
while middle_drawer.ycor() > -half_height:
    middle_drawer.pendown()
    middle_drawer.forward(20)
    middle_drawer.penup()
    middle_drawer.forward(20)

player_1 = paddle.PlayerPaddle((-350, 0))
player_2 = paddle.PlayerPaddle((350, 0))
game_ball = ball.Ball()
scoreboard = ScoreBoard()

game_on = True
while game_on:
    time.sleep(0)
    screen.update()
    game_ball.move()
    if game_ball.ycor() <= -290 or game_ball.ycor() >= 290:
        game_ball.wall_bounce()
    screen.onkey(player_2.move_up, "Up")
    screen.onkey(player_2.move_down, "Down")
    screen.onkey(player_1.move_up, "w")
    screen.onkey(player_1.move_down, "s")

    if game_ball.distance(player_2) < 50 and game_ball.xcor() > 330 or game_ball.distance(player_1) < 50 and game_ball.xcor() < -330:
        game_ball.paddle_bounce()

    if game_ball.xcor() > 400:
        game_ball.ball_reset()
        time.sleep(1)
        scoreboard.l_point()

    if game_ball.xcor() < -400:
        game_ball.ball_reset()
        time.sleep(1)
        scoreboard.r_point()


screen.exitonclick()
