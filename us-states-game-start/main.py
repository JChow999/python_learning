import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
t = turtle.Turtle()
t.hideturtle()
t.penup()

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
correct_guesses = 0
correct_guesses = 0

print(data)

game_on = True
while game_on:
    if correct_guesses == 0:
        answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    else:
        answer_state = screen.textinput(title=f"{correct_guesses}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state in all_states:
        correct_guesses += 1
        state_data = data[data["state"] == answer_state]
        t.goto(float(state_data["x"]), float(state_data["y"]))
        t.write(answer_state)
        if correct_guesses >= 50:
            game_on = False

screen.exitonclick()

