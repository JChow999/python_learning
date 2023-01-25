import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.go_to_start()

    def is_at_finish_line(self):
        return self.ycor() >= FINISH_LINE_Y

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        x_pos = self.xcor()
        y_pos = self.ycor() + MOVE_DISTANCE
        if self.ycor() < 280:
            self.goto(x_pos, y_pos)

    def move_down(self):
        x_pos = self.xcor()
        y_pos = self.ycor() - MOVE_DISTANCE
        if self.ycor() > -280:
            self.goto(x_pos, y_pos)

    def move_right(self):
        x_pos = self.xcor() + MOVE_DISTANCE
        y_pos = self.ycor()
        if self.xcor() < 280:
            self.goto(x_pos, y_pos)

    def move_left(self):
        x_pos = self.xcor() - MOVE_DISTANCE
        y_pos = self.ycor()
        if self.xcor() > -280:
            self.goto(x_pos, y_pos)
