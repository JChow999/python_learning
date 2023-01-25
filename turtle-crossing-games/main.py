import turtle
import player
import time
import car_manager
from scoreboard import ScoreBoard

current_level = 1

scoreboard = ScoreBoard()
screen = turtle.Screen()
screen.setup(600, 600)
screen.tracer(0)

character = player.Player()
car_manager = car_manager.CarManager()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    screen.listen()

    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if -15 <= character.ycor() - car.ycor() <= 15:
            if character.distance(car) <= 28:
                game_on = False
                scoreboard.game_over()
        elif character.distance(car) < 22:
            game_on = False
            scoreboard.game_over()

    #movement detection
    screen.onkey(character.move_up, "Up")
    screen.onkey(character.move_down, "Down")
    screen.onkey(character.move_left, "Left")
    screen.onkey(character.move_right, "Right")

    if character.is_at_finish_line():
        character.go_to_start()
        car_manager.level_up()
        current_level += 1
        scoreboard.level_up()


screen.exitonclick()
