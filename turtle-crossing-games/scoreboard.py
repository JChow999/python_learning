import turtle
FONT = ("Courier", 24, "normal")


class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 270)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
